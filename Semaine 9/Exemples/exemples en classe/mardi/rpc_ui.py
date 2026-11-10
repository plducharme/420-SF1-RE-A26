from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QLabel, QMainWindow, QWidget, QVBoxLayout, \
    QTextEdit, QMenu
from PySide6.QtGui import QPixmap, QAction

import rpc


class JeuRochePapierCiseaux(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Super Roche Papier Ciseaux 2026")
        self.disposition = QGridLayout()
        self.widget_central = QWidget()
        self.widget_central.setLayout(self.disposition)
        self.setCentralWidget(self.widget_central)

        self.barre_menu = self.menuBar()
        self.menu_partie = QMenu("Partie")
        self.barre_menu.addMenu(self.menu_partie)

        self.action_redemarrer = QAction("Redémarrer")
        self.action_redemarrer.triggered.connect(self.redemarrer)
        self.menu_partie.addAction(self.action_redemarrer)

        self.menu_partie.addSeparator()
        self.action_quitter = QAction("Quitter")
        self.action_quitter.triggered.connect(self.close)
        self.menu_partie.addAction(self.action_quitter)

        self.disposition_joueur = QVBoxLayout()

        self.score_joueur = 0
        self.score_cpu = 0

        grandeur_bouton = QSize(200, 100)
        grandeur_icone = QSize(64, 64)
        self.bouton_roche = QPushButton()
        self.bouton_roche.setObjectName("roche")
        self.bouton_roche.setFixedSize(grandeur_bouton)
        self.roche_pixmap = QPixmap("roche.png").scaled(QSize(64, 64))
        self.bouton_roche.setIcon(self.roche_pixmap)
        self.bouton_roche.setIconSize(grandeur_icone)
        self.bouton_roche.clicked.connect(self.jouer_clicked)
        self.disposition_joueur.addWidget(self.bouton_roche)

        self.bouton_papier = QPushButton()
        self.bouton_papier.setObjectName("papier")
        self.bouton_papier.setFixedSize(grandeur_bouton)
        self.papier_pixmap = QPixmap("papier.png").scaled(QSize(64, 64))
        self.bouton_papier.setIcon(self.papier_pixmap)
        self.bouton_papier.setIconSize(grandeur_icone)
        self.bouton_papier.clicked.connect(self.jouer_clicked)
        self.disposition_joueur.addWidget(self.bouton_papier)

        self.bouton_ciseaux = QPushButton()
        self.bouton_ciseaux.setObjectName("ciseaux")
        self.bouton_ciseaux.setFixedSize(grandeur_bouton)
        self.ciseaux_pixmap = QPixmap("ciseaux.png").scaled(QSize(64, 64))
        self.bouton_ciseaux.setIcon(self.ciseaux_pixmap)
        self.bouton_ciseaux.setIconSize(grandeur_icone)
        self.bouton_ciseaux.clicked.connect(self.jouer_clicked)
        self.disposition_joueur.addWidget(self.bouton_ciseaux)

        self.disposition.addLayout(self.disposition_joueur, 1, 1, 3, 1)

        self.log_jeu = QTextEdit()
        self.disposition.addWidget(self.log_jeu, 1, 2, 3, 1)

        self.choix_ordi = QLabel()
        self.disposition.addWidget(self.choix_ordi, 1, 3, 3, 1)

        self.scores_label = QLabel("Scores")
        self.scores_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scores_label.setStyleSheet("color: blue; font-size: 24;")
        self.disposition.addWidget(self.scores_label, 4, 1, 1, 3)

        self.score_joueur_label = QLabel("0")
        self.disposition.addWidget(self.score_joueur_label, 5, 1, 1, 1)
        self.score_cpu_label = QLabel("0")
        self.disposition.addWidget(self.score_cpu_label, 5, 3, 1, 1)

    def jouer_clicked(self):
        sender = self.sender()
        nom = sender.objectName()

        choix_cpu = rpc.choix_ordi()
        resultat = rpc.resultat(nom, choix_cpu)

        if choix_cpu == "roche":
            self.choix_ordi.setPixmap(self.roche_pixmap)
        elif choix_cpu == "papier":
            self.choix_ordi.setPixmap(self.papier_pixmap)
        else:
            self.choix_ordi.setPixmap(self.ciseaux_pixmap)

        self.log_jeu.append(f"Choix de l'ordi: {choix_cpu}")

        if resultat == 2:
            self.log_jeu.append("Vous avez perdu")
            self.score_cpu += 1
        elif resultat == 1:
            self.log_jeu.append("Vous avez gagné")
            self.score_joueur += 1
        else:
            self.log_jeu.append("Partie nulle")

        self.score_cpu_label.setText(str(self.score_cpu))
        self.score_joueur_label.setText(str(self.score_joueur))

    def redemarrer(self):
        self.score_joueur = 0
        self.score_cpu = 0

        self.score_cpu_label.setText(str(self.score_cpu))
        self.score_joueur_label.setText(str(self.score_joueur))

        self.log_jeu.clear()


app = QApplication()
rpc_app = JeuRochePapierCiseaux()
rpc_app.show()
app.exec()
