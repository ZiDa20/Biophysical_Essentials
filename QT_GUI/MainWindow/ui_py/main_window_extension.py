
#add this above the central widget
self.progressBar = QProgressBar()
self.statusBar = MainWindow.statusBar()# add Status Bar to the App
self.statusBar.addPermanentWidget(self.progressBar)
self.progressBar.setFixedWidth(200)
self.progressBar.setAlignment(Qt.AlignLeft)


#exchagne the Config widget with this and delete the self.online below
self.online = Online_Analysis()
self.config = Config_Widget(self.online, self.progressBar,  self.statusBar)