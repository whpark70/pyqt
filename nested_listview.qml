import QtQuick 2.10

Rectangle {
	width: 360
	height: 360

	ListModel {
		id: model1

		ListElement {
			name: "name"
		}
		ListElement {
			name: "name"
		}
		ListElement {
			name: "name"
		}
	}

	ListModel {
		id: model2
		ListElement {
			name: "inside"
		}
		ListElement {
			name: "inside"
		}
		ListElement {
			name: "inside"
		}
	}

	ListView {
		id: outer
		model: model1
		delegate: listdelegate
		anchors.fill: parent
	}

	Component {
		id: listdelegate

		Item {
			width: 100
			height: col.childrenRect.height

			Column {
				id: col
				anchors.left: parent.left
				anchors.right: parent.right
				Text {
					id: t1
					text: name
				}
				ListView {
					id: insidelist
					model: model2
					property  int collapseHeightFlag: childrenRect.height
					delegate: Component {
						id: delegate2

						Item {
							width: 100
							height: col2.childrenRect.height

							Column {
								id: col2
								anchors.left: parent.left
								anchors.right: parent.right
								Text {
									id: name1
									text: name
								}
							}
							MouseArea {
								anchors.fill: parent
								onClicked: {
									insidelist.currentIndex = index
								}
							}
						}
					}
					contentHeight: contentItem.childrenRect.height
					height: 0
					anchors.left: parent.left
					anchors.right: parent.right
					clip: true
					highlight: Rectangle {
						color: "pink"
						radius: 2
					}
					focus: true

				}

			}
			Rectangle {
				color: "red"
				width: 10
				height: 10
				anchors.right: parent.right
				anchors.rightMargin: 5
				anchors.top: parent.top
				anchors.topMargin: 5

				MouseArea {
					anchors.fill: parent
					onClicked: {
						if(insidelist.height == insidelist.collapseHeightFlag) {
							insidelist.height = 0
						}
						else {
							insidelist.height = insidelist.collapseHeightFlag
						}
					}
				}
			}
		}
	}
}
