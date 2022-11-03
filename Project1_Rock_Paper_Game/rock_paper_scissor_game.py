import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap  # For font and Images import
from PyQt5.QtCore import QTimer # Timer
from random import randint

textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)
computer_score = 0
player_score = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ###################Creat an Empty Window################
        self.setWindowTitle("Rock Paper Scissor Game")
        self.setGeometry(50, 50, 550, 500)
        self.UI()

    def UI(self):
        ################### QLables Scores #################
        self.comp = QLabel("Computer Score: ", self)
        self.comp.setFont(textFont)
        self.comp.move(30, 20)
        # For Score tracking
        self.scorecomp = QLabel("0", self)
        self.scorecomp.setFont(textFont)
        self.scorecomp.move(160, 20)

        self.plyr = QLabel("Player Score: ", self)
        self.plyr.setFont(textFont)
        self.plyr.move(330, 20)
        #For score tracking
        self.scoreplyr = QLabel("0", self)
        self.scoreplyr.setFont(textFont)
        self.scoreplyr.move(435, 20)

        ############# Images #######################
        self.imgcom = QLabel(self)
        self.imgcom.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/rock.png"))
        self.imgcom.move(40, 100)
        #
        self.imgplr = QLabel(self)
        self.imgplr.move(320, 100)
        self.imgplr.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/rock.png"))
        #
        self.imgvs = QLabel(self)
        self.imgvs.move(230,170)
        self.imgvs.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/game.png"))

        #################### Buttons #######################
        start = QPushButton("Start", self)
        start.move(160, 250)
        start.setFont(buttonFont)
        start.clicked.connect(self.startgm)
        # Stop Button
        stop = QPushButton("Stop", self)
        stop.move(250, 250)
        stop.setFont(buttonFont)
        stop.clicked.connect(self.stopgm)

        ################### Timer ##############
        self.timer = QTimer(self)
        self.timer.setInterval(10)
        # Connecting timer to the game
        self.timer.timeout.connect(self.playgame)

        ##########
        self.show()

    # Start the timer when hit start button
    def startgm(self):
        self.timer.start()

    # Randomly
    def playgame(self):
        # Random Images Appearance for Computer
        self.ranCom = randint(1, 3)
        if self.ranCom == 1:
            self.imgcom.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/rock.png"))
        elif self.ranCom == 2:
            self.imgcom.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/paper.png"))
        else:
            self.imgcom.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/scissors.png"))

        # Random Images Appearance for Player
        self.ranPly = randint(1, 3)
        if self.ranPly == 1:
            self.imgplr.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/rock.png"))
        elif self.ranPly == 2:
            self.imgplr.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/paper.png"))
        else:
            self.imgplr.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Project1_Rock_Paper_Game/Resources-Rock-Paper-Scissors-Game-What-We-are-Going-to-Build/scissors.png"))

    # in stop we assign all the game rules
    def stopgm(self):
        global computer_score
        global player_score
        self.timer.stop()
        # 1-- Rock
        # 2-- Paper
        # 3-- Scissor
        if self.ranCom == 1 and self.ranPly == 2:
            mbox = QMessageBox.information(self, "Information", "Player Wins")
            player_score +=1
            #print (player_score)
            self.scoreplyr.setText(format(player_score))

        elif self.ranCom == 1 and self.ranPly == 3:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computer_score +=1
            #print(computer_score)
            self.scorecomp.setText(format(computer_score))

        elif self.ranCom == 2 and self.ranPly == 1:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computer_score +=1
            #print(computer_score)
            self.scorecomp.setText(format(computer_score))

        elif self.ranCom == 2 and self.ranPly == 3:
            mbox = QMessageBox.information(self, "Information", "Player Wins")
            player_score +=1
            #print(player_score)
            self.scoreplyr.setText(format(player_score))

        elif self.ranCom == 3 and self.ranPly == 1:
            mbox = QMessageBox.information(self, "Information", "Player Wins")
            player_score +=1
            #print(player_score)
            self.scoreplyr.setText(format(player_score))

        elif self.ranCom == 3 and self.ranPly == 2:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computer_score +=1
            #print(computer_score)
            self.scorecomp.setText(format(computer_score))
        else:
            mbox = QMessageBox.information(self, "Information", "Draw")

        # Stop if any player score 3 scores
        if computer_score == 3 or player_score == 3:
           mbox= QMessageBox.information(self, "information", " Game Over")
           sys.exit()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
