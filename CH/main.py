from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\\Program Files (x86)\\chromedriver.exe"

def Query_Current_Moves(driver):
    parentElement = driver.find_element_by_class_name("layout-board.board")
    all_children_by_xpath = parentElement.find_elements_by_xpath(".//*")
    all_children_by_xpath[21].get_attribute('outerHTML')
    #[i for i in os.listdir(DATA_PATH_SEGMENTS) if i.find('.')==-1]
    pieces=[i for i in all_children_by_xpath if i.get_attribute('outerHTML').find("piece")==-1]
    print(pieces)

def main():
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.chess.com/play/computer")

    #icon - font - chess x modal - seo - close - icon

    element = driver.find_element_by_class_name("piece.wp.square-42")
    print(element.location)

    Query_Current_Moves(driver)



    #action = ActionChains(driver)
    #action.drag_and_drop_by_offset(element, 0, -100)
    #action.perform()






if __name__ == "__main__":
    main()