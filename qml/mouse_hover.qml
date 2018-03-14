import QtQuick 2.10

Background {
	width: 240
	height: 300

	property color hoverColor: "#efefef"
	property color clickColor: "lightblue"

	ListView {
		id: view
		anchors.fill: parent
		anchors.margins: 20

		clip: true

		model: 5

		delegate: numberDelegate
		spacing: 5
	}

	Component {
		id: numberDelegate

		Item {
			
			width: ListView.view.width
			height: 40
			signal clicked

			Rectangle {
				id: itemarea
				anchors.fill: parent
				
				Text {
					anchors.centerIn: parent
					font.pixelSize: 10
					text: index	
				}

				MouseArea {
					hoverEnabled: true
					anchors.fill: parent
					onEntered: { itemarea.state='Hovering' }
					onExited: { itemarea.state=''}
					onClicked: { itemarea.state="Clicked"; }
					onReleased: {
						if(containsMouse)
							itemarea.state="Hovering"
						else
							itemarea.state=""
					}
				}
				states: [
					State {
						name: "Hovering"
						PropertyChanges {
							target: itemarea
							color: hoverColor
						}
					},
					State {
						name: "Clicked"
						PropertyChanges {
							target: itemarea
							color: clickColor
						}
					}
				]

				transitions: [
					Transition {
						from: ""; to: "Hovering"
						ColorAnimation { duration: 200 }
					},
					Transition {
						from: "*"; to: "Clicked"
						ColorAnimation { duration: 100}
					}
				]

			}
			
		}
	}

	
}