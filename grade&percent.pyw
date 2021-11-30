from os import name
from kivymd.app import MDApp
from kivymd.uix import screen
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (440, 650)
kv = '''
ScreenManager:
    Start:
    Design:
<Start>
    name:'start'
    MDRoundFlatButton:
        text: "Start"
        font_style:'H6'
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        text_color: 0, 1, 0, 1
        on_release:
            root.manager.current='see'
            root.manager.transition.direction='left'
<Design>
    name:'see'
    MDLabel:
        text: 'FIND  GARDE  &&  PERCENT'
        theme_text_color:'Custom'
        text_color:'black'
        pos_hint:{'center_y':0.9}
        halign:'center'
        font_style:'H5'
    MDTextField:
        id:eng
        helper_text:'Required'
        text_align:'center'
        hint_text:"English"
        pos_hint: {'center_x':0.3,'center_y':0.7}
        size_hint: (0.3,0.1)
    MDTextField:
        id:nep
        text_align:'center'
        hint_text:"Nepali"
        pos_hint: {'center_x':0.7,'center_y':0.7}
        size_hint: (0.3,0.1)


    MDTextField:
        id:math
        text_align:'center'
        hint_text:"Mathmatics"
        pos_hint: {'center_x':0.3,'center_y':0.6}
        size_hint: (0.3,0.1)
    MDTextField:
        id:sc
        text_align:'center'
        hint_text:"Science"
        pos_hint: {'center_x':0.7,'center_y':0.6}
        size_hint: (0.3,0.1)




    MDTextField:
        id:so
        text_align:'center'
        hint_text:"Social Std"
        pos_hint: {'center_x':0.3,'center_y':0.5}
        size_hint: (0.3,0.1)
    MDTextField:
        id:opt
        text_align:'center'
        hint_text:"OPT Math"
        pos_hint: {'center_x':0.7,'center_y':0.5}
        size_hint: (0.3,0.1)


    MDTextField:
        id:occu
        text_align:'center'
        hint_text:"Occupation"
        pos_hint: {'center_x':0.3,'center_y':0.4}
        size_hint: (0.3,0.1)
    MDTextField:
        id:com
        text_align:'center'
        hint_text:"Computer"
        pos_hint: {'center_x':0.7,'center_y':0.4}
        size_hint: (0.3,0.1)

    MDRectangleFlatButton:
        
        pos_hint: {'center_x':0.5,'center_y':0.3}
        md_bg_color:app.theme_cls.primary_color
        text:'Result'
        on_release:app.Find()


    MDLabel:
        text:'Pecent % ::'
        halign:'center'
        pos_hint: {'center_x':0.5,'center_y':0.2}
    MDLabel:
        id: percent
        text:'-  -  -  -'
        halign:'center'
        pos_hint: {'center_x':0.6,'center_y':0.2}




    MDLabel:
        text:'Grade :: '
        halign:'center'
        pos_hint: {'center_x':0.5,'center_y':0.1}
    MDLabel:
        id:grade
        text:'-  -  -  -'
        halign:'center'
        pos_hint: {'center_x':0.6,'center_y':0.1}
        
        
'''


class Start(Screen):
    pass


class Design(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Start(name='start'))
sm.add_widget(Design(name='see'))


class Grade(MDApp):
    def build(self):

        screen = Screen()
        self.style = Builder.load_string(kv)
        screen.add_widget(self.style)
        return screen
# The Program IS Coded By Basanta chaudhary
# 
    def Find(self):
        eng = int(self.style.get_screen('see').ids.eng.text)
        english = int(eng)
        nep = self.style.get_screen('see').ids.nep.text
        nepali = int(nep)
        mt = self.style.get_screen('see').ids.math.text
        math = int(mt)
        sc = self.style.get_screen('see').ids.sc.text
        science = int(sc)
        so = self.style.get_screen('see').ids.so.text
        social = int(so)
        ot = self.style.get_screen('see').ids.opt.text
        opt = int(ot)
        occu = self.style.get_screen('see').ids.occu.text
        occupation = int(occu)
        com = self.style.get_screen('see').ids.com.text
        computer = int(com)
        total = int(english+nepali+math+science+social+opt+occupation+computer)
        per = int(total/8)
        gd = ''
        if per >= 90 and per <= 100:
            gd = 'A+'

        elif per >= 80 and per <= 90:
            gd = 'A'
        elif per >= 70 and per <= 80:
            gd = 'B+'
        elif per >= 60 and per <= 70:
            gd = 'B'
        elif per >= 50 and per <= 60:
            gd = 'C+'
        elif per >= 40 and per <= 50:
            gd = 'C'
        elif per >= 30 and per <= 40:
            gd = 'D+'
        elif per >= 20 and per <= 30:
            gd = 'D'
        elif per >= 10 and per <= 20:
            gd = 'E+'
        elif per >= 0 and per <= 10:
            gd = 'E'
        print(gd)
        k = str(per)

        self.style.get_screen('see').ids.percent.text = k
        self.style.get_screen('see').ids.grade.text = gd

   # def grade(self):


Grade().run()
