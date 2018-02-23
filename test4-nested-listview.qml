import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Window 2.10

ApplicationWindow {
	x: 100
	y: 100
	width: 1024
	height: 768
	visible: true
	
	ListView {
		id: list
		anchors.fill: parent
		model: myModel
		delegate: nodeDelegate
	}

	Component {
		id: nodeDelegate

		Rectangle {
			width: 50; height: 10
			Column {
				Text { text: node}
				
			}
			MouseArea {
				anchors.fill: parent
				onClicked: console.log(list.currentIndex)
			}

				
		}
		
	}
}
