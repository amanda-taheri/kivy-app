from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class Percentage (MDApp):
        def build(self):
                screen = Screen()
                table = MDDataTable(
                    size_hint=(0.7, 0.7),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    column_data=[
                        ("   No.", dp(20)),
                        ("Lessons", dp(30)),
                        ("scores", dp(30)),
                        ("Test Date" , dp(30)),
                        
                       
                        ],

                    row_data=[
                        ("   1", "math", "18", "1399/04/24"),
                        ("   2", "chem", "17.5", "1400/04/07"),
                    ])

                table.bind(on_check_press=self.check_press)
                table.bind(on_row_press=self.row_press)
                screen.add_widget(table)
                return screen

        def check_press(self, instance_table, current_row):
                print(instance_table, current_row)

        def row_press(self, instance_table, instance_row):
                print(instance_table, instance_row)


Percentage().run()
