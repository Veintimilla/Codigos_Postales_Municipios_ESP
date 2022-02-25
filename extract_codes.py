import io

import pandas as pd

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from webdriver_manager.firefox import GeckoDriverManager

WEB_ROOT = "https://www.solosequenosenada.com"

class ExtractPostalCodes():
    
    def __init__(self):
        self.url = "https://www.solosequenosenada.com/2010/09/16/listado-de-todos-los-codigos-postales-de-espana/"

    def _get_driver(self):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        return driver

    def run(self):
        try:
            self.driver = self._get_driver()
            self.driver.get(self.url)
            self.driver.find_element_by_xpath("/html/body/aside/div/div/div[2]/button[2]").click()  # Closing cookies windows 
            element = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/article/div/p[6]")
            link_element_list = element.find_elements_by_tag_name("a")
            link_element_dict = {x.text: x.get_attribute("href") for x in link_element_list}
            final_df = None
            
            for key, value in link_element_dict.items():
                self.driver.get(value)
                province_codes = self.driver.find_element_by_xpath("/html/body/p[3]").text
                province_df = pd.read_csv(io.StringIO(province_codes), header=None, sep='\t')
                province_df.rename(columns={0: "data"}, inplace=True)
                province_df['codigo_postal'] = province_df["data"].apply(lambda x: x.split(" ")[0])
                province_df['nombre'] = province_df['data'].apply(lambda x: " ".join(x.split(" ")[1:]))
                province_df['nombre'] = province_df['nombre'].str.replace("El código varía según la calle", "")
                province_df.drop(['data'], axis=1, inplace=True)
                province_df['provincia'] = key
                if final_df is None:
                    final_df = province_df
                else:
                    final_df = pd.concat([final_df, province_df], axis=0, ignore_index=True)
            final_df.to_csv("codigos_postales_municipales.csv", index=False, encoding='utf-8')
        except Exception as e:
            print("Something went wrong: {}".format(e))

        finally:
            self.driver.close()

if __name__ == "__main__":
    bot = ExtractPostalCodes()
    bot.run()