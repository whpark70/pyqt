import QtQuick 2.10
import QtQuick.Controls 2.3

ApplicationWindow {
	x: 100
	y: 100
	width: 640
	height: 480
	visible: true
	title: "QtQuick Test"

	Item {
		width: 200
		height: 480

		ListView {
			id: list
			anchors.fill: parent
			model: nestedModel
			delegate: categoryDelegate
		}

		ListModel {
			id: nestedModel
			ListElement {
				categoryName: "Veggies"
				collapsed: true
				subItems: [
					ListElement {
						itemName: "Toamto"
					},
					ListElement {
						itemName: "Cucumber"
					}
				]
			}
		}

		Component {
			id: categoryDelegate
			Column {
				width: 200

				Rectangle {
					id: categoryItem
					border.color: "black"
					border.width: 1
					height: 30
					width: 200
					Text {
						x: 15
						anchors.verticalCenter: parent.verticalCenter
						font.pixelSize:14
						text: categoryName
					}
					Rectangle {
						color: "red"
						width: 20
						height: 20
						anchors.right : parent.right
						anchors.rightMargin: 10
						anchors.verticalCenter: parent.verticalCenter

						MouseArea {
							anchors.fill: parent
							onClicked: {
								list.currentIndex = index
								nestedModel.setProperty(index, "collapsed", !collapsed)
							}
						}
					}
				}

				Loader {
					id: subItemLoader
					visible: !collapsed
					property variant subItemModel: subItems
					//sourceComponent: collapsed ? null: subItemColumnDelegate
					sourceComponent: subItemColumnDelegate
					onStatusChanged: if (status == Loader.Ready) item.model = subItemModel
				}
			}

		}

		Component {
			id: subItemColumnDelegate
			Column {
				property alias model: subItemRepeater.model
				width: 200
				Repeater {
					id: subItemRepeater
					delegate: Rectangle {
						x: 10
						height: 30
						width: 190
						Text {
							anchors.verticalCenter: parent.verticalCenter
							x: 30
							font.pixelSize: 11
							text: itemName
						}
					}
				}
			}
		}
	}
}