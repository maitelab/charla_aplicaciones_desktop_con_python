import QtQuick 2.0
import QtQuick.Window 2.0
import QtWebEngine 1.0

Window {
    width: 1024
    height: 768
    visible: true
    WebEngineView {
        anchors.fill: parent
        url: "https://www.funkykarts.rocks/demo.html"
    }
}
