import QtQuick 2.10

Item {
	id: root
	width: 1024; height: 768

	ListModel {
		id: animalsModel
		ListElement { name: "Puss in Boots"; type: "Cats"; aVisible: false }
		ListElement { name: "Bengal"; type: "Cats"; aVisible: false }
		ListElement { name: "Pug"; type: "Dogs"; aVisible: false }
		ListElement { name: "German Shepherd"; type: "Dogs"; aVisible: false}
		ListElement { name: "Parrot"; type: "Birds"}
	}

	Component {
		id: sectionHeader
		Rectangle {
			id: testRect
			width: 100
			height: 50
			color: "green"

			Text {
				text: section
				anchors.centerIn: parent
			}

			MouseArea {
				anchors.fill: parent
				onClicked: {
					console.log("clicked")
					for(var i=0; i<animalsModel.count; i++) 
					{
						var animal = animalsModel.get(i);
						if(animal.type == section && animal.aVisible == false) {
							animal.aVisible = true;
							testRect.color = "red"
						}
						else if(animal.type == section && animal.aVisible == true) {
							animal.aVisible = false;
							testRect.color = "green"
						}
						else {
							animal.aVisible = false
						}

					}
				}	
			}
		}
	}

	ListView {
		id: listing
		width: 100
		height: parent.height
		model: animalsModel
		delegate: listdelegate

		section.property: "type"
		section.criteria: ViewSection.FullString
		section.delegate: sectionHeader
	}

	Component {
		id: listdelegate

		Rectangle {
			id: menuItem
			width: 100
			height: 55
			color: ListView.isCurrentItem ? "light blue" : "white"
			visible: aVisible

			onVisibleChanged: {
				if(visible) 
					height = 55;
				else	
					height = 0;
			}

			Behavior on height {
				NumberAnimation { duration: 1 }
			}

			Text {
				id: text
				text: name
				anchors.centerIn: parent
			}

			MouseArea {
				anchors.fill: parent
				onClicked: {
					listing.currentIndex = index
				}
			}
		}

	}
}