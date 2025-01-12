from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Whatsappbot:

    def __init__(self):
        self.WPP_URL = "https://web.whatsapp.com/"
        self.NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div/span'
        self.SEARCH_CONTACT = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]'
        self.FIRST_CONTACT= '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span'
        self.TYPE_MSG = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        self.SEND_BUTTON = '//*[@id="main"]/footer/div[1]/div[3]/button/span'
        self.OPTION_BTN = "(//div[contains(@class,'message-out')]//div[@role='button'])[last()]"
        self.DIALOG_OPTION = '//div[contains(@class, "QhSbI")]'
        self.OPTION_DELETE = '//*[@id="app"]/div[1]/span[4]/div/ul/div/li[5]'
        self.DELETE_BTN = "(//div[@data-animate-modal-popup='true']//div[@role='button'])[last()]"
        self.FIRST_DIALOG_BTN = '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div[2]'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.WPP_URL)
    
    def send_message(self,contato,mensagem):
        """
            Will send a message via selenium to the indicated contact
        Parameters
        ----------
        contato : Enter the name of the contact or group
            Enter the name of the contact or group you want to send the message to, you can use a for or while for more than one group or contact
        mensagem : Enter the message to be sent
            Type the message you want to use, you can use a for or while for more than one message.

        Returns
        -------
        None.

        """
        #Open new chat on whatsapp web
        new_msg_button = self.driver.find_element_by_xpath(self.NEW_CHAT)
        new_msg_button.click()
        sleep(1)
        #Search the contact
        search_field = self.driver.find_element_by_xpath(self.SEARCH_CONTACT)
        search_field.click()
        search_field.send_keys(contato)
        sleep(1)
        #Click on the firts contact with the name that I told        
        first_contact = self.driver.find_element_by_xpath(self.FIRST_CONTACT)
        first_contact.click()
        sleep(1.5)
        type_field = self.driver.find_element_by_xpath(self.TYPE_MSG)
        type_field.click()
        type_field.send_keys(mensagem)
        send_msg= self.driver.find_element_by_xpath(self.SEND_BUTTON)
        send_msg.click()
        sleep(1)
    
    def delete_message(self,contato):
        """
         This function will delete the last message sent.
        Parameters
        ----------
        contato : Enter the name of the contact or group
            Enter the name of the contact or group you want to send the message to, you can use a for or while for more than one group or contact

        Returns
        -------
        None.

        """
        #Open new chat on whatsapp web
        new_msg_button = self.driver.find_element_by_xpath(self.NEW_CHAT)
        new_msg_button.click()
        sleep(1)
        #Search the contact
        search_field = self.driver.find_element_by_xpath(self.SEARCH_CONTACT)
        search_field.click()
        search_field.send_keys(contato)
        sleep(1)
        #Click on the firts contact with the name that I told
        first_contact = self.driver.find_element_by_xpath(self.FIRST_CONTACT)
        first_contact.click()
        sleep(1.5)
        #open the dialog by clicking this button
        btn_option = self.driver.find_element_by_xpath(self.OPTION_BTN)  
        hover = ActionChains(self.driver).move_to_element(btn_option)
        hover.perform()
        dialog_click = self.driver.find_element_by_xpath(self.DIALOG_OPTION)
        dialog_click.click()
        sleep(1.5)
        #Then select Delete message option by clicking on
        btn_option_delete = self.driver.find_element_by_xpath(self.OPTION_DELETE)
        btn_option_delete.click()
        sleep(1.5)
        #delete that message for everyone
        delete = self.driver.find_element_by_xpath(self.DELETE_BTN)
        delete.click()
        sleep(1)
        #Confirm the option
        #Criar opção para checar se aparece a caixa de diálogo
        try:
            self.driver.find_element_by_xpath(self.FIRST_DIALOG_BTN).click()
        except:
            pass