import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"
# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()


#test how many images is displayed and the links to other pages in the top navigation bar
class SearchTests(unittest.TestCase):

   def test_homepage_image(self):
   # Navigate to the application home page
      driver.get("https://www.gamesquare.app/")
   # get the list of elements which are displayed after the search
   # currently on result page using find_elements_by_class_name method
      lists = driver.find_elements_by_class_name("item")

   # get the number of elements found
      print ("Found " + str(len(lists)) + " searches:")
      i=0
      for listitem in lists:
         print (listitem.get_attribute("innerHTML"))
         i=i+1
         if(i>10):
            break

      assert "No results found." not in driver.page_source

      flag = driver.find_element_by_link_text('Home').is_displayed()
      if flag == 1:
           print("displayed")
      else:
           print("link error")

      flag = driver.find_element_by_link_text('Consoles').is_displayed()
      if flag == 1:
           print("displayed")
      else:
           print("link error")

      flag = driver.find_element_by_link_text('Search Games').is_displayed()
      if flag == 1:
           print("displayed")
      else:
           print("link error")

      flag = driver.find_element_by_link_text('Rating').is_displayed()
      if flag == 1:
           print("displayed")
      else:
           print("link error")

      flag = driver.find_element_by_link_text('About').is_displayed()
      if flag == 1:
           print("displayed")
      else:
           print("link error")


      driver.quit()


#test the link connected to the individual console page
class ButtonTests(unittest.TestCase):
   def test_console_link_to_page(self):
      driver.get("https://www.gamesquare.app/consoles")
      element = driver.find_element_by_id("1")
      element.click()
      print("clicked")
      driver.get("https://www.gamesquare.app/consoles")
      element = driver.find_element_by_id("2")
      element.click()
      print("clicked")
      driver.get("https://www.gamesquare.app/consoles")
      element = driver.find_element_by_id("3")
      element.click()
      print("clicked")
      driver.get("https://www.gamesquare.app/consoles")
      element = driver.find_element_by_id("4")
      element.click()
      print("clicked")
      driver.get("https://www.gamesquare.app/consoles")
      element = driver.find_element_by_id("5")
      element.click()
      print("clicked")
      driver.get("https://www.gamesquare.app/consoles")
      element = driver.find_element_by_id("6")
      element.click()
      print("clicked")
      driver.quit()


# test if the link works in about page
class AboutPageTests(unittest.TestCase):
   def test_about_link(self):
       driver.get("https://www.gamesquare.app/about")

       flag = driver.find_element_by_link_text('GitHub Repository').is_displayed()
       if flag == 1:
            print("displayed")
       else:
            print("link error")

       flag = driver.find_element_by_link_text('Nintendo Switch').is_displayed()
       if flag == 1:
           print("displayed")
       else:
           print("link error")

       flag = driver.find_element_by_link_text('XBOX').is_displayed()
       if flag == 1:
           print("displayed")
       else:
           print("link error")

       flag = driver.find_element_by_link_text('Play Station').is_displayed()
       if flag == 1:
           print("displayed")
       else:
           print("link error")

       driver.quit()


#test search button in games page
class GameTests(unittest.TestCase):
   def test_game_button(self):
       driver.get("https://www.gamesquare.app/index")
       driver.find_element_by_xpath("//input[@type='submit' and @value='Search']").click()
       print("clicked and displayed")
       driver.quit()

if __name__ == "__main__":
    unittest.main()