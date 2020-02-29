from bs4 import BeautifulSoup
import requests

def parse_faq():
    URL = 'https://pk.mipt.ru/faq/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    questions = soup.find(id='question_list')
    q_list = questions.findAll('div', class_='q_question')
    a_list = questions.findAll('div', class_='t_answer')

    q_dict = {
            "Бакалавриат": [],
            "Магистратура": [],
            "Прочее": []
        }

    for quest, ans in zip(q_list, a_list):
        q_cat = str(quest.find('div', class_='q_cat').text)
        if not q_cat in ["Бакалавриат", "Магистратура"]:
            q_cat = "Прочее"
        q_date        = quest.find('span', class_='q_date').text
        q_title       = quest.find('div',  class_='q_title').text
        q_description = quest.find('div',  class_='q_description').text

        q_dict[q_cat].append(
                {
                    "date":        q_date,
                    "title":       q_title,
                    "description": q_description,
                    "ans":         ans.text
                }
            )

    return q_dict

#
#
#
#  def main():
#      parse_faq()
#
#
#
#  if __name__ == '__main__':
    #  main()
