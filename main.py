from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
kv="""
ScreenManager:
    SimpleScreen:
    NameScreen:
    TextScreen:
    

<DrawerClickableItem@MDNavigationDrawerItem>

<TextScreen>:
    name:'text'
    text:"it is text screen"
    MDRectangleFlatButton:
        text:'home'
        halign:"center"
        on_press:root.manager.current='Simple'
<SimpleScreen>:
    name:'Simple'

    MDTextField:
        hint_text:"Enter your username"
        helper_text:"username must be uniqe"
        helper_text_mode:"on_focus"
        icon_left:"account-circle"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Enter your password"
        helper_text:"password must be 6 chareter"
        helper_text_mode:"on_focus"
        icon_left:"lock"
        pos_hint:{"center_x":0.5,"center_y":0.4}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text:"LogIn"
        pos_hint:{"center_x":0.5,"center_y":0.3}
        text_color:(1,0,0,1)
        on_press:root.manager.current='text'
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    title:" Itdude"
                    elivation:4
                    pos_hint:{"top":1}
                    left_action_items:[['menu',lambda x:nav_drawer.set_state("open")]]
        MDNavigationDrawer:
            id:nav_drawer
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title:"Chuder Vai"
                    text:"@dula vai"
                    spacing:"4dp"
                    padding:"12dp",0,0,"44dp"
                MDNavigationDrawerLabel:
                    text:"menu"
                DrawerClickableItem:
                    icon:"gmail"
                    text:"Inbox"
                    on_press:root.manager.current='name'

                DrawerClickableItem:
                    id:"name"
                    icon:"folder"
                    text:"all"
                    on_press:root.manager.current='name'
                MDNavigationDrawerLabel:
                    text:"all.."
                DrawerClickableItem:
                    icon:"send"
                    text:"hello"
                    on_press:root.manager.current='name'
                DrawerClickableItem:
                    icon:"send"
                    text:"hello"
                    on_press:root.manager.current='name'

<NameScreen>:
    name:'name'
    text:'simple screen'
    MDRectangleFlatButton:
        text:"simple"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_press:root.manager.current='Simple'



"""
#<NavigationDrawerItem@MDNavigationDrawerItem>
class NameScreen(Screen):
    pass
class SimpleScreen(Screen):
    pass
class TextScreen(Screen):
    pass

sm=ScreenManager()
sm.add_widget(NameScreen(name='name'))
sm.add_widget(SimpleScreen(name='Simple'))
sm.add_widget(TextScreen(name='text'))
class x5(MDApp):
    def build(self):
        bldr= Builder.load_string(kv)
        return bldr
x5().run()