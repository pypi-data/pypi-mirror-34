/****************************************************************************
**
** Copyright (C) 2017 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the Qt Quick Controls 2 module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL3$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see http://www.qt.io/terms-conditions. For further
** information use the contact form at http://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or later as published by the Free
** Software Foundation and appearing in the file LICENSE.GPL included in
** the packaging of this file. Please review the following information to
** ensure the GNU General Public License version 2.0 requirements will be
** met: http://www.gnu.org/licenses/gpl-2.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Controls.impl 2.4
import QtQuick.Templates 2.4 as T
import QtQuick.Controls.Material 2.4

T.Tumbler {
    id: control
    implicitWidth: 60
    implicitHeight: 200

    delegate: Text {
        text: modelData
        color: control.Material.foreground
        font: control.font
        opacity: (1.0 - Math.abs(Tumbler.displacement) / (control.visibleItemCount / 2)) * (control.enabled ? 1 : 0.6)
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    contentItem: TumblerView {
        model: control.model
        delegate: control.delegate
        path: Path {
            startX: contentItem.width / 2
            startY: -contentItem.delegateHeight / 2
            PathLine {
                x: contentItem.width / 2
                y: (control.visibleItemCount + 1) * contentItem.delegateHeight - contentItem.delegateHeight / 2
            }
        }

        property real delegateHeight: control.availableHeight / control.visibleItemCount
    }
}
