import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: Screen.width
    height: 30
    y: 0
    flags: Qt.FramelessWindowHint

    Rectangle {
        anchors.fill: parent
        color: "#1e1e1e"

        Text {
            anchors.centerIn: parent
            text: "Per Screen Panel – Dev"
            color: "white"
        }
    }
}
