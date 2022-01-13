def DOMinate(URL="", sleeptime=3, filen=None):

    # GET THE SOUP
    if filen != None:
        try:
            # TODO - if the file is not there, is still runs and gives a stupid error about soup variable...
            outfile = open(filen)
            soup = BeautifulSoup(outfile, 'lxml')
            sleeptime = 0 # no need to wait!
            print("getting the DOM from file")
        except:
            print(f"could not get DOM info from file: {filen}")

    else: # get it on the internet...
        print(f"Dominating {URL}")
        opts = Options()
        opts.add_argument(" --headless")
        driver = webdriver.Chrome( chromedriverpath , options=opts)
        # BUG - SQUASH THIS ANNOYING BULLSHIT PLZZ....
        #./DOMinate.py:51: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
        # driver = webdriver.Chrome( chromedriverpath , options=opts)

        try:
            driver.get(URL)
        except WebDriverException:
            print("driver.get(URL) threw an exception - maybe the website is down")
            exit(1)
        #TODO - log success here

        print(f"napping for {sleeptime} seconds so the DOM can cook...")
        time.sleep( sleeptime )
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, 'lxml') # or html
        driver.quit()



    # MEAT AND POTATOES OF THE FUNCTION
    allUnits = []
    try:

        csv_columns = ["Certified Reseller:","Hosted in:","Second Hand:","Name",\
            "Price:","Hashrate:","Energy Cons:","Minimum Order:","Online date:",\
                "Shipping date:","Link:"]

        # NO TOUCH OR PAPA NO KISS!
        FLAG_USA = """viewBox='0 0 7410"""
        FLAG_RUS = """viewBox='0 0 9"""
        FLAG_CAN = """viewBox='0 0 1000"""
        with open(csv_file, 'w') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()

            for g in soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['flex','flex-col','w-full','lg:pr-4','pb-4','pt-6','h-full']):

                unit = {"Certified Reseller:":"No",
                        "Hosted in:":"at home",
                        "Second Hand:":'new', # should be undetermined... but it works for now (do not assume state)
                        "Name":0,
                        "Price:":0,
                        "Hashrate:":0,
                        "Energy Cons:":0,
                        "Minimum Order:":0,
                        "Online date:":0,
                        "Shipping date:":0,
                        "Link:":0}

                if "Compass Certified Reseller" in g.text:
                    unit["Certified Reseller:"] = "Yes"

                if "Hand" in g.text: # && "Second" (logical, not bitwise operand?)
                    unit["Second Hand:"] = 'used'

                # LINK
                # ['w-full','relative','pb-5/10','overflow-hidden','rounded-15px','cursor-pointer']
                lnk = g.find(lambda tag: tag.name == 'div' and tag.get('class') == ['w-full','relative','pb-5/10','overflow-hidden','rounded-15px','cursor-pointer']).get('href')
                unit['Link:'] = "https://compassmining.io" + lnk

                # <p class="pt-1 text-sm font-bold leading-none font-sans">Hosted in </p>
                a = g.find(lambda tag: tag.name == 'p' and tag.get('class') == ['pt-1','text-sm','font-bold','leading-none','font-sans'])
                if "Hosted in" in a.text:
                    if FLAG_USA in str(a.next_sibling.next):
                        unit['Hosted in:'] = "USA"
                    if FLAG_RUS in str(a.next_sibling.next):
                        unit['Hosted in:'] = "RUS" #putin is a bitch
                    if FLAG_CAN in str(a.next_sibling.next):
                        unit['Hosted in:'] = "CAN"

                # UNIT NAME
                #<h3 class="text-xl font-bold font-sans">Antminer S19j Pro 100 TH </h3></div>
                #['text-xl','font-bold','font-sans']
                a = g.find(lambda tag: tag.name == 'h3' and tag.get('class') == ['text-xl','font-bold','font-sans'])
                unit['Name'] = a.text

                # Price:
                # Hashrate:
                # Energy Cons:
                # Minimum Order:
                #<p class="text-sm leading-none font-sans text-graphite mr-2 w-29">
                #['text-sm','leading-none','font-sans','text-graphite','mr-2','w-29']
                for a in g.find_all(lambda tag: tag.name == 'p' and tag.get('class') == ['text-sm','leading-none','font-sans','text-graphite','mr-2','w-29']):
                    if stripUnits == True:
                        unit[a.text] = int( re.sub("[^0-9]","",a.next_sibling.text) ) # REMOVE UNITS (ALL NON NUMERALS)
                    else:
                        unit[a.text] = a.next_sibling.text

                a = g.find(lambda tag: tag.name == 'p' and tag.get('class') == ['mr-2','text-sm','leading-none','pt-2px','font-sans','w-29','text-graphite'])
                unit[a.text] = a.next_sibling.text

                #print(unit)
                writer.writerow(unit)
                allUnits.append(unit)
    except IOError:
        # TODO CATCH EVERYTHING..
        # TODO - IF THERE IS A BREAK IN THE WEB SCRAPING (PERHAPS FROM COMPASS UPDATING THEIR WEBSITE), THEN IT NEEDS TO REFLECT IN A DEBUG LOG
        print("yo dog, your code borked.. ok man?\n")
    return allUnits
