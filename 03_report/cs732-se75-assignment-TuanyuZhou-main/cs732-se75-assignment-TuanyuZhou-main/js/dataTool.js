(function (global, factory) {
	typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports, require('echarts')) :
	typeof define === 'function' && define.amd ? define(['exports', 'echarts'], factory) :
	(factory((global.dataTool = {}),global.echarts));
}(this, (function (exports,echarts) { 'use strict';



var arrayProto = Array.prototype;
var nativeMap = arrayProto.map;


function map(obj, cb, context) {
    if (!(obj && cb)) {
        return;
    }
    if (obj.map && obj.map === nativeMap) {
        return obj.map(cb, context);
    }
    else {
        var result = [];
        for (var i = 0, len = obj.length; i < len; i++) {
            result.push(cb.call(context, obj[i], i, obj));
        }
        return result;
    }
}

function parse(xml) {
    var doc;
    if (typeof xml === 'string') {
        var parser = new DOMParser();
        doc = parser.parseFromString(xml, 'text/xml');
    }
    else {
        doc = xml;
    }
    if (!doc || doc.getElementsByTagName('parsererror').length) {
        return null;
    }

    var gexfRoot = getChildByTagName(doc, 'gexf');

    if (!gexfRoot) {
        return null;
    }

    var graphRoot = getChildByTagName(gexfRoot, 'graph');

    var attributes = parseAttributes(getChildByTagName(graphRoot, 'attributes'));
    var attributesMap = {};
    for (var i = 0; i < attributes.length; i++) {
        attributesMap[attributes[i].id] = attributes[i];
    }

    return {
        nodes: parseNodes(getChildByTagName(graphRoot, 'nodes'), attributesMap),
        links: parseEdges(getChildByTagName(graphRoot, 'edges'))
    };
}

function parseAttributes(parent) {
    return parent ? map(getChildrenByTagName(parent, 'attribute'), function (attribDom) {
        return {
            id: getAttr(attribDom, 'id'),
            title: getAttr(attribDom, 'title'),
            type: getAttr(attribDom, 'type')
        };
    }) : [];
}

function parseNodes(parent, attributesMap) {
    return parent ? map(getChildrenByTagName(parent, 'node'), function (nodeDom) {

        var id = getAttr(nodeDom, 'id');
        var label = getAttr(nodeDom, 'label');

        var node = {
            id: id,
            name: label,
            itemStyle: {
                normal: {}
            }
        };

        var vizSizeDom = getChildByTagName(nodeDom, 'viz:size');
        var vizPosDom = getChildByTagName(nodeDom, 'viz:position');
        var vizColorDom = getChildByTagName(nodeDom, 'viz:color');
        // var vizShapeDom = getChildByTagName(nodeDom, 'viz:shape');

        var attvaluesDom = getChildByTagName(nodeDom, 'attvalues');

        if (vizSizeDom) {
            node.symbolSize = parseFloat(getAttr(vizSizeDom, 'value'));
        }
        if (vizPosDom) {
            node.x = parseFloat(getAttr(vizPosDom, 'x'));
            node.y = parseFloat(getAttr(vizPosDom, 'y'));
            // z
        }
        if (vizColorDom) {
            node.itemStyle.normal.color = 'rgb(' +[
                getAttr(vizColorDom, 'r') | 0,
                getAttr(vizColorDom, 'g') | 0,
                getAttr(vizColorDom, 'b') | 0
            ].join(',') + ')';
        }
        // if (vizShapeDom) {
            // node.shape = getAttr(vizShapeDom, 'shape');
        // }
        if (attvaluesDom) {
            var attvalueDomList = getChildrenByTagName(attvaluesDom, 'attvalue');

            node.attributes = {};

            for (var j = 0; j < attvalueDomList.length; j++) {
                var attvalueDom = attvalueDomList[j];
                var attId = getAttr(attvalueDom, 'for');
                var attValue = getAttr(attvalueDom, 'value');
                var attribute = attributesMap[attId];

                if (attribute) {
                    switch (attribute.type) {
                        case 'integer':
                        case 'long':
                            attValue = parseInt(attValue, 10);
                            break;
                        case 'float':
                        case 'double':
                            attValue = parseFloat(attValue);
                            break;
                        case 'boolean':
                            attValue = attValue.toLowerCase() == 'true';
                            break;
                        default:
                    }
                    node.attributes[attId] = attValue;
                }
            }
        }

        return node;
    }) : [];
}

function parseEdges(parent) {
    return parent ? map(getChildrenByTagName(parent, 'edge'), function (edgeDom) {
        var id = getAttr(edgeDom, 'id');
        var label = getAttr(edgeDom, 'label');

        var sourceId = getAttr(edgeDom, 'source');
        var targetId = getAttr(edgeDom, 'target');

        var edge = {
            id: id,
            name: label,
            source: sourceId,
            target: targetId,
            lineStyle: {
                normal: {}
            }
        };

        var lineStyle = edge.lineStyle.normal;

        var vizThicknessDom = getChildByTagName(edgeDom, 'viz:thickness');
        var vizColorDom = getChildByTagName(edgeDom, 'viz:color');
        // var vizShapeDom = getChildByTagName(edgeDom, 'viz:shape');

        if (vizThicknessDom) {
            lineStyle.width = parseFloat(vizThicknessDom.getAttribute('value'));
        }
        if (vizColorDom) {
            lineStyle.color = 'rgb(' + [
                getAttr(vizColorDom, 'r') | 0,
                getAttr(vizColorDom, 'g') | 0,
                getAttr(vizColorDom, 'b') | 0
            ].join(',') + ')';
        }
        // if (vizShapeDom) {
        //     edge.shape = vizShapeDom.getAttribute('shape');
        // }

        return edge;
    }) : [];
}

function getAttr(el, attrName) {
    return el.getAttribute(attrName);
}

function getChildByTagName (parent, tagName) {
    var node = parent.firstChild;

    while (node) {
        if (
            node.nodeType != 1 ||
            node.nodeName.toLowerCase() != tagName.toLowerCase()
        ) {
            node = node.nextSibling;
        } else {
            return node;
        }
    }

    return null;
}

function getChildrenByTagName (parent, tagName) {
    var node = parent.firstChild;
    var children = [];
    while (node) {
        if (node.nodeName.toLowerCase() == tagName.toLowerCase()) {
            children.push(node);
        }
        node = node.nextSibling;
    }

    return children;
}


var gexf = (Object.freeze || Object)({
	parse: parse
});



var quantile = function(ascArr, p) {
    var H = (ascArr.length - 1) * p + 1,
        h = Math.floor(H),
        v = +ascArr[h - 1],
        e = H - h;
    return e ? v + e * (ascArr[h] - v) : v;
};


function asc(arr) {
    arr.sort(function (a, b) {
        return a - b;
    });
    return arr;
}

var prepareBoxplotData = function (rawData, opt) {
    opt = opt || [];
    var boxData = [];
    var outliers = [];
    var axisData = [];
    var boundIQR = opt.boundIQR;
    var useExtreme = boundIQR === 'none' || boundIQR === 0;

    for (var i = 0; i < rawData.length; i++) {
        axisData.push(i + '');
        var ascList = asc(rawData[i].slice());

        var Q1 = quantile(ascList, 0.25);
        var Q2 = quantile(ascList, 0.5);
        var Q3 = quantile(ascList, 0.75);
        var min = ascList[0];
        var max = ascList[ascList.length - 1];

        var bound = (boundIQR == null ? 1.5 : boundIQR) * (Q3 - Q1);

        var low = useExtreme
            ? min
            : Math.max(min, Q1 - bound);
        var high = useExtreme
            ? max
            : Math.min(max, Q3 + bound);

        boxData.push([low, Q1, Q2, Q3, high]);

        for (var j = 0; j < ascList.length; j++) {
            var dataItem = ascList[j];
            if (dataItem < low || dataItem > high) {
                var outlier = [i, dataItem];
                opt.layout === 'vertical' && outlier.reverse();
                outliers.push(outlier);
            }
        }
    }
    return {
        boxData: boxData,
        outliers: outliers,
        axisData: axisData
    };
};


var version = '1.0.0';


if (echarts.dataTool) {
    echarts.dataTool.version = version;
    echarts.dataTool.gexf = gexf;
    echarts.dataTool.prepareBoxplotData = prepareBoxplotData;
}

exports.version = version;
exports.gexf = gexf;
exports.prepareBoxplotData = prepareBoxplotData;

})));
