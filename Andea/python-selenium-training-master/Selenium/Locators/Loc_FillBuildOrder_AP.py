from selenium.webdriver.common.by import By


class Loc_FillBuildOrder_AP():
    # locator to Standard Login link
    DDN_PLM_PROJECT = By.XPATH, "//span[contains(@id,'GetInputs_PLMProjectID')]"
    DDN_PLM_PROJECT2 = By.XPATH, "//input[@class='select2-search__field']"
    # DDN_PLM_PROJECT3 = By.XPATH, "//li[contains(@class='results__option--highlighted']"
    # DDN_PLM_PROJECT3 = By.XPATH, "//li[contains(text(),'188901 AHO GPM INF IF DEV')]"
    DDN_PLM_PROJECT3 = By.XPATH, "//ul[contains(@id,'GetInputs_PLMProjectID')]//li[1]"
    # DDN_PLM_PROJECT3 = By.XPATH, "//ul[contains(@id,'GetInputs_PLMProjectID')]"
    # DDN_PLM_PROJECT4 = By.CSS_SELECTOR, "select2-ctl03_ctl00_G0_G33_G49_2_GetInputs_PLMProjectID_1034_0_Editor-results > li"
    # select2-ctl03_ctl00_G0_G33_G49_2_GetInputs_PLMProjectID_1034_0_Editor-results > li
    # Alternate Engineer
    DDN_ALTER_ENGIN = By.XPATH, "//span[contains(@id,'GetInputs_AltEngineerEmployeeID')]"
    DDN_ALTER_ENGIN2 = By.XPATH, "//input[@class='select2-search__field']"
    DDN_ALTER_ENGIN3 = By.XPATH, "//li[contains(@id,'GetInputs_AltEngineerEmployeeID')]"
    # AFIS Number
    TXT_AFIS_NUM = By.XPATH, "//input[contains(@id,'AFISNumber')]"
    # Cost Center
    TXT_COST_CEN = By.XPATH, "// span[contains(@id, 'GetInputs_CostCenter')]"
    TXT_COST_CEN2 = By.XPATH, "//li[contains(@id,'GetInputs_CostCenter')]"
    # End Use Designation- Internal
    RDO_INTER_USE = By.XPATH, "//label[contains(text(),'Internal')]"
    # Category
    DDN_CATEGORY = By.XPATH, "//span[contains(@id,'GetInputs_ProductGroup')]"
    DDN_CATEGORY2 = By.XPATH, "//input[@class='select2-search__field']"
    DDN_CATEGORY3 = By.XPATH, "//li[contains(text(),'Airbag')]"
    # Part number
    DDN_PART_NUM = By.XPATH, "//span[contains(@id,'GetInputs_ProductID')]"
    DDN_PART_NUM2 = By.XPATH, "//input[@class='select2-search__field']"
    DDN_PART_NUM3 = By.XPATH, "//li[starts-with(text(),'X644146100A-00-02- - RETRACTOR')]"
    # Facility
    DDN_FACILITY = By.XPATH, "//span[contains(@id,'GetInputs_Facility')]"
    DDN_FACILITY2 = By.XPATH, "//input[@class='select2-search__field']"
    DDN_FACILITY3 = By.XPATH, "//li[contains(@title,'ABR')]"