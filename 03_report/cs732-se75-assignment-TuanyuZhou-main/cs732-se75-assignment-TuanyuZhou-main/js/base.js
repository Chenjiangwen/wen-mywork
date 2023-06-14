$(function () {
    echart_map();
    function echart_1() {
        var myChart = echarts.init(document.getElementById('chart_1'));
        myChart.clear();
        option = {
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c}"
            },
            legend: {
                x: 'center',
                y: '15%',
                data: ['Changsha', 'Zhuzhou', 'Xiangtan', 'Hengyang', 'Shaoyang', 'yueyang', 'changde', 'Zhangjiajie', 'yiyang', 'Chenzhou', 'Yongzhou', 'Loudi', 'Huaihua', 'Xiangxi'],
                icon: 'circle',
                textStyle: {
                    color: '#fff',
                }
            },
            calculable: true,
            series: [{
                name: '',
                type: 'pie',
                startAngle: 0,
                radius: [41, 280.75],
                center: ['50%', '40%'],
                roseType: 'area',
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: true,
                        formatter: '{c}'
                    },
                    emphasis: {
                        show: true
                    }
                },
                labelLine: {
                    normal: {
                        show: true,
                        length2: 1,
                    },
                    emphasis: {
                        show: true
                    }
                },
                data: [{
                    value: 900.58,
                    name: 'Huaihua',
                    itemStyle: {
                        normal: {
                            color: '#f845f1'
                        }
                    }
                },
                {
                    value: 1100.58,
                    name: 'Yongzhou',
                    itemStyle: {
                        normal: {
                            color: '#ad46f3'
                        }
                    }
                },
                {
                    value: 1200.58,
                    name: 'Zhangjiajie',
                    itemStyle: {
                        normal: {
                            color: '#5045f6'
                        }
                    }
                },
                {
                    value: 1300.58,
                    name: 'Shaoyang',
                    itemStyle: {
                        normal: {
                            color: '#4777f5'
                        }
                    }
                },
                {
                    value: 1400.58,
                    name: 'changde',
                    itemStyle: {
                        normal: {
                            color: '#44aff0'
                        }
                    }
                },
                {
                    value: 1500.58,
                    name: 'yueyang',
                    itemStyle: {
                        normal: {
                            color: '#45dbf7'
                        }
                    }
                },
                {
                    value: 1500.58,
                    name: 'Xiangtan',
                    itemStyle: {
                        normal: {
                            color: '#f6d54a'
                        }
                    }
                },
                {
                    value: 1600.58,
                    name: 'Zhuzhou',
                    itemStyle: {
                        normal: {
                            color: '#f69846'
                        }
                    }
                },
                {
                    value: 1800,
                    name: 'Changsha',
                    itemStyle: {
                        normal: {
                            color: '#ff4343'
                        }
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: '#transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                },
                {
                    value: 0,
                    name: "",
                    itemStyle: {
                        normal: {
                            color: 'transparent'
                        }
                    },
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                }
                ]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
    function echart_0() {
        var myChart = echarts.init(document.getElementById('chart_0'));

        function showProvince() {
                var geoCoordMap = {
                    'Changsha Huanghua International Airport': [113.226512,28.192929],
                    'Zhangjiajie Lotus Airport': [110.454598,29.107223],
                    'Changde Taohuayuan Airport': [111.651508,28.921516],
                    'Yongzhou Lingling Airport': [111.622869,26.340994],
                    'zhijiang airport': [109.714784,27.44615],
                };
                var data = [{
                        name: 'Changsha Huanghua International Airport',
                        value: 100
                    },
                    {
                        name: 'Zhangjiajie Lotus Airport',
                        value: 100
                    },
                    {
                        name: 'Changde Taohuayuan Airport',
                        value: 100
                    },
                    {
                        name: 'Yongzhou Lingling Airport',
                        value: 100
                    },
                    {
                        name: 'zhijiang airport',
                        value: 100
                    }
                ];
                var max = 480,
                    min = 9; // todo 
                var maxSize4Pin = 100,
                    minSize4Pin = 20;
                var convertData = function (data) {
                    var res = [];
                    for (var i = 0; i < data.length; i++) {
                        var geoCoord = geoCoordMap[data[i].name];
                        if (geoCoord) {
                            res.push({
                                name: data[i].name,
                                value: geoCoord.concat(data[i].value)
                            });
                        }
                    }
                    return res;
                };

                myChart.setOption(option = {
                    title: {
                        top: 20,
                        text: '',
                        subtext: '',
                        x: 'center',
                        textStyle: {
                            color: '#ccc'
                        }
                    },
                    legend: {
                        orient: 'vertical',
                        y: 'bottom',
                        x: 'right',
                        data: ['pm2.5'],
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    visualMap: {
                        show: false,
                        min: 0,
                        max: 500,
                        left: 'left',
                        top: 'bottom',
                        text: ['高', '低'],
                        calculable: true,
                        seriesIndex: [1],
                        inRange: {
                        }
                    },
                    geo: {
                        show: true,
                        map:'hunan',
                        mapType: 'hunan',
                        label: {
                            normal: {
                            },
                            emphasis: {
                                textStyle: {
                                    color: '#fff'
                                }
                            }
                        },
                        roam: true,
                        itemStyle: {
                            normal: {
                                //          	color: '#ddd',
                                borderColor: 'rgba(147, 235, 248, 1)',
                                borderWidth: 1,
                                areaColor: {
                                    type: 'radial',
                                    x: 0.5,
                                    y: 0.5,
                                    r: 0.8,
                                    colorStops: [{
                                        offset: 0,
                                        color: 'rgba(175,238,238, 0)'
                                    }, {
                                        offset: 1,
                                        color: 'rgba(	47,79,79, .2)'
                                    }],
                                    globalCoord: false
                                },
                                shadowColor: 'rgba(128, 217, 248, 1)',
                                shadowOffsetX: -2,
                                shadowOffsetY: 2,
                                shadowBlur: 10
                            },
                            emphasis: {
                                areaColor: '#389BB7',
                                borderWidth: 0
                            }
                        }
                    },
                    series: [{
                            name: 'light',
                            type: 'map',
                            coordinateSystem: 'geo',
                            data: convertData(data),
                            itemStyle: {
                                normal: {
                                    color: '#F4E925'
                                }
                            }
                        },
                        {
                            name: '点',
                            type: 'scatter',
                            coordinateSystem: 'geo',
                            symbol: 'pin',
                            symbolSize: function(val) {
                                var a = (maxSize4Pin - minSize4Pin) / (max - min);
                                var b = minSize4Pin - a * min;
                                b = maxSize4Pin - a * max;
                                return a * val[2] + b;
                            },
                            label: {
                                normal: {
                                    // show: true,
                                    // textStyle: {
                                    //     color: '#fff',
                                    //     fontSize: 9,
                                    // }
                                }
                            },
                            itemStyle: {
                                normal: {
                                    color: '#F62157',
                                }
                            },
                            zlevel: 6,
                            data: convertData(data),
                        },
                        {  
                            name: 'light',
                            type: 'map',
                            mapType: 'hunan',
                            geoIndex: 0,
                            aspectScale: 0.75,
                            showLegendSymbol: false,
                            label: {
                                normal: {
                                    show: false
                                },
                                emphasis: {
                                    show: false,
                                    textStyle: {
                                        color: '#fff'
                                    }
                                }
                            },
                            roam: true,
                            itemStyle: {
                                normal: {
                                    areaColor: '#031525',
                                    borderColor: '#FFFFFF',
                                },
                                emphasis: {
                                    areaColor: '#2B91B7'
                                }
                            },
                            animation: false,
                            data: data
                        },
                        {
                            name: ' ',
                            type: 'effectScatter',
                            coordinateSystem: 'geo',
                            data: convertData(data.sort(function (a, b) {
                                return b.value - a.value;
                            }).slice(0, 5)),
                            symbolSize: function (val) {
                                return val[2] / 10;
                            },
                            showEffectOn: 'render',
                            rippleEffect: {
                                brushType: 'stroke'
                            },
                            hoverAnimation: true,
                            label: {
                                normal: {
                                    formatter: '{b}',
                                    position: 'right',
                                    show: true
                                }
                            },
                            itemStyle: {
                                normal: {
                                    color: '#05C3F9',
                                    shadowBlur: 10,
                                    shadowColor: '#05C3F9'
                                }
                            },
                            zlevel: 1
                        },

                    ]
                });
        }
        showProvince();

        // myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
    function echart_2() {
        var myChart = echarts.init(document.getElementById('chart_2'));

            myChart.setOption({
                series: [{
                    type: 'map',
                    mapType: 'hunan'
                }]
            });

            var geoCoordMap = {
                'Huaihua': [109.999867,27.518949],
                'Jishou': [109.741528,28.332629],
                'Zhangjiajie': [110.491722,29.112001],
                'changde': [111.701486,29.076683],
                'yiyang': [112.348741,28.544124],
                'yueyang': [113.126486,29.382401],
                'Changsha': [113.019455,28.200103],
                'Zhuzhou': [113.163141,27.8418],
                'Xiangtan': [112.91977,27.882141],
                'Shaoyang': [111.467859,27.21915],
                'Loudi': [112.012438,27.745506],
                'Hengyang': [112.63809,26.895225],
                'Yongzhou': [111.577632,26.460144],
                'Chenzhou': [113.039396,25.81497]
            };

            var goData = [
                [{
                    name: 'Zhangjiajie'

                }, {
                    id: 1,
                    name: 'changde',
                    value: 86
                }],
                [{
                    name: 'Jishou'

                }, {
                    id: 1,
                    name: 'changde',
                    value: 86
                }],
                [{
                    name: 'changde'

                }, {
                    id: 1,
                    name: 'yiyang',
                    value: 70
                }],
                [{
                    name: 'yiyang'

                }, {
                    id: 1,
                    name: 'Changsha',
                    value: 95
                }],
                [{
                    name: 'Changsha'

                }, {
                    id: 1,
                    name: 'yueyang',
                    value: 70
                }],
                [{
                    name: 'Changsha'

                }, {
                    id: 1,
                    name: 'Xiangtan',
                    value: 80
                }],
                [{
                    name: 'Changsha'

                }, {
                    id: 1,
                    name: 'Zhuzhou',
                    value: 80
                }],
                [{
                    name: 'Changsha'

                }, {
                    id: 1,
                    name: 'Hengyang',
                    value: 80
                }],
                [{
                    name: 'Hengyang'

                }, {
                    id: 1,
                    name: 'Chenzhou',
                    value: 70
                }],
                [{
                    name: 'Hengyang'

                }, {
                    id: 1,
                    name: 'Yongzhou',
                    value: 70
                }],
                [{
                    name: 'Xiangtan'

                }, {
                    id: 1,
                    name: 'Loudi',
                    value: 60
                }],
                [{
                    name: 'Loudi'

                }, {
                    id: 1,
                    name: 'Shaoyang',
                    value: 75
                }],
                [{
                    name: 'Shaoyang'

                }, {
                    id: 1,
                    name: 'Huaihua',
                    value: 75
                }],
            ];
            var backData = [
                [{
                    name: 'changde'

                }, {
                    id: 1,
                    name: 'Zhangjiajie',
                    value: 80
                }],
                [{
                    name: 'changde'

                }, {
                    id: 1,
                    name: 'Jishou',
                    value: 66
                }],
                [{
                    name: 'yiyang'

                }, {
                    id: 1,
                    name: 'changde',
                    value: 86
                }],
                [{
                    name: 'Changsha'

                }, {
                    id: 1,
                    name: 'yiyang',
                    value: 70
                }],
                [{
                    name: 'yueyang'

                }, {
                    id: 1,
                    name: 'Changsha',
                    value: 95
                }],
                [{
                    name: 'Xiangtan'

                }, {
                    id: 1,
                    name: 'Changsha',
                    value: 95
                }],
                [{
                    name: 'Zhuzhou'

                }, {
                    id: 1,
                    name: 'Changsha',
                    value: 95
                }],
                [{
                    name: 'Hengyang'

                }, {
                    id: 1,
                    name: 'Changsha',
                    value: 95
                }],
                [{
                    name: 'Chenzhou'

                }, {
                    id: 1,
                    name: 'Hengyang',
                    value: 80
                }],
                [{
                    name: 'Yongzhou'

                }, {
                    id: 1,
                    name: 'Hengyang',
                    value: 80
                }],
                [{
                    name: 'Loudi'

                }, {
                    id: 1,
                    name: 'Xiangtan',
                    value: 80
                }],
                [{
                    name: 'Shaoyang'

                }, {
                    id: 1,
                    name: 'Loudi',
                    value: 60
                }],
                [{
                    name: 'Huaihua'

                }, {
                    id: 1,
                    name: 'Shaoyang',
                    value: 75
                }],
            ];

            var planePath = 'path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z';
            var arcAngle = function(data) {
                var j, k;
                for (var i = 0; i < data.length; i++) {
                    var dataItem = data[i];
                    if (dataItem[1].id == 1) {
                        j = 0.2;
                        return j;
                    } else if (dataItem[1].id == 2) {
                        k = -0.2;
                        return k;
                    }
                }
            }

            var convertData = function(data) {
                var res = [];
                for (var i = 0; i < data.length; i++) {
                    var dataItem = data[i];
                    var fromCoord = geoCoordMap[dataItem[0].name];
                    var toCoord = geoCoordMap[dataItem[1].name];
                    if (dataItem[1].id == 1) {
                        if (fromCoord && toCoord) {
                            res.push([{
                                coord: fromCoord,
                            }, {
                                coord: toCoord,
                                value: dataItem[1].value

                            }]);
                        }
                    } else if (dataItem[1].id == 2) {
                        if (fromCoord && toCoord) {
                            res.push([{
                                coord: fromCoord,
                            }, {
                                coord: toCoord
                            }]);
                        }
                    }
                }
                return res;
            };

            var color = ['#fff', '#FF1493', '#0000FF'];
            var series = [];
            [
                ['1', goData],
                ['2', backData]
            ].forEach(function(item, i) {
                series.push({
                    name: item[0],
                    type: 'lines',
                    zlevel: 2,
                    symbol: ['arrow', 'arrow'],
                    effect: {
                        show: true,
                        period: 6,
                        trailLength: 0.1,
                        symbol: 'arrow',
                        symbolSize: 5
                    },
                    lineStyle: {
                        normal: {
                            width: 1,
                            opacity: 0.4,
                            curveness: arcAngle(item[1]),
                            color: '#fff'
                        }
                    },
                    edgeLabel: {
                        normal: {
                            show: true,
                            textStyle: {
                                fontSize: 14
                            },
                            formatter: function(params) {
                                var txt = '';
                                if (params.data.speed !== undefined) {
                                    txt = params.data.speed;
                                }
                                return txt;
                            },
                        }
                    },
                    data: convertData(item[1])
                }, {
                    type: 'effectScatter',
                    coordinateSystem: 'geo',
                    zlevel: 2,
                    rippleEffect: {
                        period: 2,
                        brushType: 'stroke',
                        scale: 3
                    },
                    label: {
                        normal: {
                            show: true,
                            color: '#fff',
                            position: 'right',
                            formatter: '{b}'
                        }
                    },
                    symbol: 'circle',
                    symbolSize: function(val) {
                        return val[2] / 8;
                    },
                    itemStyle: {
                        normal: {
                            show: true
                        }
                    },
                    data: item[1].map(function(dataItem) {
                        return {
                            name: dataItem[1].name,
                            value: geoCoordMap[dataItem[1].name].concat([dataItem[1].value])
                        };
                    })

                });

            });

            option = {
                title: {
                    text: '',
                    subtext: '',
                    left: 'center',
                    textStyle: {
                        color: '#fff'
                    }
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{b}'
                },
                visualMap: {
                    show: false,
                    min: 0,
                    max: 100,
                    color: ['#31A031','#31A031']
                },
                geo: {
                    map: 'hunan',
                    zoom: 1,
                    label: {
                        normal: {
                            show: false,
                            textStyle: {
                                color: '#fff'
                            }
                        },
                        emphasis: {
                            textStyle: {
                                color: '#fff'
                            }
                        }
                    },
                    roam: true,
                    itemStyle: {
                        normal: {
                            //          	color: '#ddd',
                            borderColor: 'rgba(147, 235, 248, 1)',
                            borderWidth: 1,
                            areaColor: {
                                type: 'radial',
                                x: 0.5,
                                y: 0.5,
                                r: 0.8,
                                colorStops: [{
                                    offset: 0,
                                    color: 'rgba(175,238,238, 0)'
                                }, {
                                    offset: 1,
                                    color: 'rgba(	47,79,79, .2)'
                                }],
                                globalCoord: false
                            },
                            shadowColor: 'rgba(128, 217, 248, 1)',
                            // shadowColor: 'rgba(255, 255, 255, 1)',
                            shadowOffsetX: -2,
                            shadowOffsetY: 2,
                            shadowBlur: 10
                        },
                        emphasis: {
                            areaColor: '#389BB7',
                            borderWidth: 0
                        }
                    }
                },
                series: series
            };
            myChart.setOption(option);
    }
    function echart_map() {
         var myChart = echarts.init(document.getElementById('chart_map'));

         var mapName = 'china'
         var data = []
         var toolTipData = [];
 
         myChart.showLoading();
         var mapFeatures = echarts.getMap(mapName).geoJson.features;
         myChart.hideLoading();
         var geoCoordMap = {
             'Fuzhou': [119.4543, 25.9222],
             'Changchun': [125.8154, 44.2584],
             'Chongqing': [107.7539, 30.1904],
             'Xian': [109.1162, 34.2004],
             'Chengdu': [103.9526, 30.7617],
             'Changzhou': [119.4543, 31.5582],
             'Beijing': [116.4551, 40.2539],
             'Beihai ': [109.314, 21.6211],
             'Haikou': [110.3893, 19.8516],
             'Changsha': [113.019455,28.200103],
             'Shanghai': [121.40, 31.73],
             'neimenggu': [106.82, 39.67]
         };
 
         var GZData = [
             [{
                 name: 'Changsha'
             }, {
                 name: 'Fuzhou',
                 value: 95
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Changchun',
                 value: 80
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Chongqing',
                 value: 70
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Xian',
                 value: 60
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Chengdu',
                 value: 50
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Changzhou',
                 value: 40
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Beijing',
                 value: 30
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Beihai ',
                 value: 20
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Haikou',
                 value: 10
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'Shanghai',
                 value: 80
             }],
             [{
                 name: 'Changsha'
             }, {
                 name: 'neimenggu',
                 value: 80
             }]
         ];
 
         var convertData = function (data) {
             var res = [];
             for (var i = 0; i < data.length; i++) {
                 var dataItem = data[i];
                 var fromCoord = geoCoordMap[dataItem[0].name];
                 var toCoord = geoCoordMap[dataItem[1].name];
                 if (fromCoord && toCoord) {
                     res.push({
                         fromName: dataItem[0].name,
                         toName: dataItem[1].name,
                         coords: [fromCoord, toCoord]
                     });
                 }
             }
             return res;
         };
 
         var color = ['#c5f80e'];
         var series = [];
         [
             ['Shijiazhuang', GZData]
         ].forEach(function (item, i) {
             series.push({
                 name: item[0],
                 type: 'lines',
                 zlevel: 2,
                 symbol: ['none', 'arrow'],
                 symbolSize: 10,
                 effect: {
                     show: true,
                     period: 6,
                     trailLength: 0,
                     symbol: 'arrow',
                     symbolSize: 5
                 },
                 lineStyle: {
                     normal: {
                         color: color[i],
                         width: 1,
                         opacity: 0.6,
                         curveness: 0.2
                     }
                 },
                 data: convertData(item[1])
             }, {
                 name: item[0],
                 type: 'effectScatter',
                 coordinateSystem: 'geo',
                 zlevel: 2,
                 rippleEffect: {
                     brushType: 'stroke'
                 },
                 label: {
                     normal: {
                         show: true,
                         position: 'right',
                         formatter: '{b}'
                     }
                 },
                 symbolSize: function (val) {
                     return val[2] / 8;
                 },
                 itemStyle: {
                     normal: {
                         color: color[i]
                     }
                 },
                 data: item[1].map(function (dataItem) {
                     return {
                         name: dataItem[1].name,
                         value: geoCoordMap[dataItem[1].name].concat([dataItem[1].value])
                     };
                 })
             });
         });
 
         option = {
             tooltip: {
                 trigger: 'item'
             },
             geo: {
                 map: 'china',
                 label: {
                     emphasis: {
                         show: false
                     }
                 },
                 roam: true,
                 itemStyle: {
                     normal: {
                         //          	color: '#ddd',
                         borderColor: 'rgba(147, 235, 248, 1)',
                         borderWidth: 1,
                         areaColor: {
                             type: 'radial',
                             x: 0.5,
                             y: 0.5,
                             r: 0.8,
                             colorStops: [{
                                 offset: 0,
                                 color: 'rgba(175,238,238, 0)'
                             }, {
                                 offset: 1,
                                 color: 'rgba(	47,79,79, .1)'
                             }],
                             globalCoord: false
                         },
                         shadowColor: 'rgba(128, 217, 248, 1)',
                         // shadowColor: 'rgba(255, 255, 255, 1)',
                         shadowOffsetX: -2,
                         shadowOffsetY: 2,
                         shadowBlur: 10
                     },
                     emphasis: {
                         areaColor: '#389BB7',
                         borderWidth: 0
                     }
                 }
             },
             series: series
         };
 
         myChart.setOption(option);
         window.addEventListener("resize", function () {
             myChart.resize();
         });
 
    }
    function echart_3() {
        var myChart = echarts.init(document.getElementById('chart_3'));
        myChart.clear();
        option = {
            
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data:['Railway transportation industry','Highway transportation industry','Water transportation industry','Air transportation industry',
                    'Pipeline transportation industry','Loading, unloading, handling, and other transportation services',
                    'Extraordinary highway mileage'],
                textStyle:{
                    color: '#fff'
                },
                top: '4%'
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            toolbox: {
                orient: 'vertical',
                right: '1%',
                top: '2%',
                iconStyle: {
                    color: '#FFEA51',
                    borderColor: '#FFA74D',
                    borderWidth: 1,
                },
                feature: {
                    saveAsImage: {},
                    magicType: {
                        show: true,
                        type: ['line','bar','stack','tiled']
                    }
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['2018','2019','2020','2021','2022'],
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: {
                name: '人',
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            color: ['#FF4949','#FFA74D','#FFEA51','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1'],
            series: [
                {
                    name:'Railway transportation industry',
                    type:'line',
                    data:[57197, 51533, 57000, 58150, 55748]
                },
                {
                    name:'Highway transportation industry',
                    type:'line',
                    data:[148054, 150198, 144943, 138157, 114234]
                },
                {
                    name:'Water transportation industry',
                    type:'line',
                    data:[27100, 25568, 25734, 24393, 23851]
                },
                {
                    name:'Air transportation industry',
                    type:'line',
                    data:[1795, 3306, 4151, 5538, 4766]
                },
                {
                    name:'Pipeline transportation industry',
                    type:'line',
                    data:[1586,567,647,1235,1186]
                },
                {
                    name:'Loading, unloading, handling, and other transportation services',
                    type:'line',
                    data:[4448, 11742, 12706, 10666, 10902]
                }
            ]
        };
        myChart.setOption(option);
    }
    function echart_4() {
     var myChart = echarts2.init(document.getElementById('chart_4'));
     var effect = {
         show: true,
         scaleSize: 1,
         period: 30,
         color: '#fff',
         shadowColor: 'rgba(220,220,220,0.4)',
         shadowBlur: 5
     };

     function itemStyle(idx) {
         return {
             normal: {
                 color: '#fff',
                 borderWidth: 1,
                 borderColor: ['rgba(30,144,255,1)', 'lime'][idx],
                 lineStyle: {
                     //shadowColor : ['rgba(30,144,255,1)','lime'][idx],
                     //shadowBlur: 10,
                     //shadowOffsetX: 0,
                     //shadowOffsetY: 0,
                     type: 'solid'
                 }
             }
         }
     };
     option = {
         color: ['rgba(30,144,255,1)', 'lime'],
         title: {
             text: '',
             subtext: '',
             sublink: '',
             x: 'center',
             textStyle: {
                 color: '#fff'
             }
         },
         tooltip: {
             trigger: 'item',
             formatter: '{b}'
         },
         legend: {
             orient: 'vertical',
             x: '2%',
             y: '3%',
             selectedMode: 'single',
             data: ['Eight vertical channels', 'Eight horizontal channels'],
             textStyle: {
                 color: '#fff'
             }
         },
         toolbox: {
             show: true,
             orient: 'vertical',
             x: 'right',
             y: 'center',
             padding: [0 ,30, 0 ,0],
             feature: {
                 mark: {
                     show: true
                 },
                 dataView: {
                     show: true,
                     readOnly: false
                 },
                 restore: {
                     show: true
                 },
                 saveAsImage: {
                     show: true
                 }
             }
         },
         series: [{
                 name: 'Eight vertical channels',
                 type: 'map',
                 roam: true,
                 hoverable: false,
                 mapType: 'china',
                 itemStyle: {
                     normal: {
                         borderColor: 'rgba(100,149,237,1)',
                         borderWidth: 0.5,
                         areaStyle: {
                             color: '#1b1b1b'
                         }
                     }
                 },
                 data: [],
                 markLine: {
                     symbol: ['circle', 'circle'],
                     symbolSize: 1,
                     effect: effect,
                     itemStyle: itemStyle(0),
                     smooth: true,
                     data: [
                         [{
                             name: 'Beijing'
                         }, {
                             name: 'Harbin'
                         }],
                         [{
                             name: 'Harbin'
                         }, {
                             name: '满洲里'
                         }],

                         [{
                             name: 'Shenyang'
                         }, {
                             name: 'Dalian'
                         }],
                         [{
                             name: 'Dalian'
                         }, {
                             name: 'Yantai'
                         }],
                         [{
                             name: 'Yantai'
                         }, {
                             name: '青岛'
                         }],
                         [{
                             name: '青岛'
                         }, {
                             name: 'Huaian'
                         }],
                         [{
                             name: 'Huaian'
                         }, {
                             name: 'Shanghai'
                         }],
                         [{
                             name: 'Shanghai'
                         }, {
                             name: 'Hangzhou'
                         }],
                         [{
                             name: 'Hangzhou'
                         }, {
                             name: 'ningbo'
                         }],
                         [{
                             name: 'ningbo'
                         }, {
                             name: 'Wenzhou'
                         }],
                         [{
                             name: 'Wenzhou'
                         }, {
                             name: 'Fuzhou'
                         }],
                         [{
                             name: 'Fuzhou'
                         }, {
                             name: 'Xiamen'
                         }],
                         [{
                             name: 'Xiamen'
                         }, {
                             name: 'Guangzhou'
                         }],
                         [{
                             name: 'Guangzhou'
                         }, {
                             name: 'Zhanjiang'
                         }],

                         [{
                             name: 'Beijing'
                         }, {
                             name: 'Tianjin'
                         }],
                         [{
                             name: 'Tianjin'
                         }, {
                             name: 'Jinan'
                         }],
                         [{
                             name: 'Jinan'
                         }, {
                             name: 'Nanjing'
                         }],
                         [{
                             name: 'Nanjing'
                         }, {
                             name: 'Shanghai'
                         }],

                         [{
                             name: 'Beijing'
                         }, {
                             name: 'Nanchang'
                         }],
                         [{
                             name: 'Nanchang'
                         }, {
                             name: 'Shenzhen'
                         }],
                         [{
                             name: 'Shenzhen'
                         }, {
                             name: '九龙红磡'
                         }],

                         [{
                             name: 'Beijing'
                         }, {
                             name: 'Zhengzhou'
                         }],
                         [{
                             name: 'Zhengzhou'
                         }, {
                             name: 'wuhan'
                         }],
                         [{
                             name: 'wuhan'
                         }, {
                             name: 'Guangzhou'
                         }],

                         [{
                             name: 'Datong'
                         }, {
                             name: 'Taiyuan'
                         }],
                         [{
                             name: 'Taiyuan'
                         }, {
                             name: 'Jiaozuo'
                         }],
                         [{
                             name: 'Jiaozuo'
                         }, {
                             name: 'Luoyang'
                         }],
                         [{
                             name: 'Luoyang'
                         }, {
                             name: 'Liuzhou '
                         }],
                         [{
                             name: 'Liuzhou '
                         }, {
                             name: 'Zhanjiang'
                         }],

                         [{
                             name: 'Baotou'
                         }, {
                             name: 'Xian'
                         }],
                         [{
                             name: 'Xian'
                         }, {
                             name: 'Chongqing'
                         }],
                         [{
                             name: 'Chongqing'
                         }, {
                             name: 'Guiyang'
                         }],
                         [{
                             name: 'Guiyang'
                         }, {
                             name: 'Liuzhou '
                         }],
                         [{
                             name: 'Liuzhou '
                         }, {
                             name: 'Nanning'
                         }],

                         [{
                             name: 'Lanzhou'
                         }, {
                             name: 'Chengdu'
                         }],
                         [{
                             name: 'Chengdu'
                         }, {
                             name: 'Kunming'
                         }]
                     ]
                 }
             },
             {
                 name: 'Eight horizontal channels',
                 type: 'map',
                 mapType: 'china',
                 itedmStyle: {
                     normal: {
                         borderColor: 'rgba(100,149,237,1)',
                         borderWidth: 0.5,
                         areaStyle: {
                             color: '#1b1b1b'
                         }
                     }
                 },
                 data: [],
                 markLine: {
                     symbol: ['circle', 'circle'],
                     symbolSize: 1,
                     effect: effect,
                     itemStyle: itemStyle(1),
                     smooth: true,
                     data: [
                         [{
                             name: 'Beijing'
                         }, {
                             name: 'Lanzhou'
                         }],
                         [{
                             name: 'Lanzhou'
                         }, {
                             name: 'Lhasa'
                         }],

                         [{
                             name: 'Datong'
                         }, {
                             name: 'qinghuangdao'
                         }],

                         [{
                             name: '神木'
                         }, {
                             name: '黄骅'
                         }],

                         [{
                             name: 'Taiyuan'
                         }, {
                             name: 'Texas'
                         }],
                         [{
                             name: 'Texas'
                         }, {
                             name: '龙口'
                         }],
                         [{
                             name: '龙口'
                         }, {
                             name: 'Yantai'
                         }],

                         [{
                             name: 'Taiyuan'
                         }, {
                             name: 'Texas'
                         }],
                         [{
                             name: 'Texas'
                         }, {
                             name: 'Jinan'
                         }],
                         [{
                             name: 'Jinan'
                         }, {
                             name: '青岛'
                         }],

                         [{
                             name: 'Changzh'
                         }, {
                             name: 'Handan'
                         }],
                         [{
                             name: 'Handan'
                         }, {
                             name: 'Jinan'
                         }],
                         [{
                             name: 'Jinan'
                         }, {
                             name: '青岛'
                         }],

                         [{
                             name: '瓦塘'
                         }, {
                             name: 'Linfen'
                         }],
                         [{
                             name: 'Linfen'
                         }, {
                             name: 'Changzh'
                         }],
                         [{
                             name: 'Changzh'
                         }, {
                             name: '汤阴'
                         }],
                         [{
                             name: '汤阴'
                         }, {
                             name: '台前'
                         }],
                         [{
                             name: '台前'
                         }, {
                             name: '兖州'
                         }],
                         [{
                             name: '兖州'
                         }, {
                             name: 'Rizhao'
                         }],

                         [{
                             name: '侯马'
                         }, {
                             name: '月山'
                         }],
                         [{
                             name: '月山'
                         }, {
                             name: '新乡'
                         }],
                         [{
                             name: '新乡'
                         }, {
                             name: '兖州'
                         }],
                         [{
                             name: '兖州'
                         }, {
                             name: 'Rizhao'
                         }],

                         [{
                             name: 'Lianyungang'
                         }, {
                             name: 'Zhengzhou'
                         }],
                         [{
                             name: 'Zhengzhou'
                         }, {
                             name: 'Lanzhou'
                         }],
                         [{
                             name: 'Lanzhou'
                         }, {
                             name: 'Urumqi'
                         }],
                         [{
                             name: 'Urumqi'
                         }, {
                             name: 'Alashankou'
                         }],

                         [{
                             name: 'Xian'
                         }, {
                             name: '南阳'
                         }],
                         [{
                             name: '南阳'
                         }, {
                             name: '信阳'
                         }],
                         [{
                             name: '信阳'
                         }, {
                             name: 'hefei'
                         }],
                         [{
                             name: 'hefei'
                         }, {
                             name: 'Nanjing'
                         }],
                         [{
                             name: 'Nanjing'
                         }, {
                             name: '启东'
                         }],

                         [{
                             name: 'Chongqing'
                         }, {
                             name: 'wuhan'
                         }],
                         [{
                             name: 'wuhan'
                         }, {
                             name: 'Jiujiang'
                         }],
                         [{
                             name: 'Jiujiang'
                         }, {
                             name: '铜陵'
                         }],
                         [{
                             name: '铜陵'
                         }, {
                             name: 'Nanjing'
                         }],
                         [{
                             name: 'Nanjing'
                         }, {
                             name: 'Shanghai'
                         }],

                         [{
                             name: 'Shanghai'
                         }, {
                             name: 'Huaihua'
                         }],
                         [{
                             name: 'Huaihua'
                         }, {
                             name: 'Chongqing'
                         }],
                         [{
                             name: 'Chongqing'
                         }, {
                             name: 'Chengdu'
                         }],
                         [{
                             name: 'Chengdu'
                         }, {
                             name: 'Guiyang'
                         }],
                         [{
                             name: 'Guiyang'
                         }, {
                             name: 'Kunming'
                         }],

                         [{
                             name: 'Kunming'
                         }, {
                             name: 'Nanning'
                         }],
                         [{
                             name: 'Nanning'
                         }, {
                             name: '黎塘'
                         }],
                         [{
                             name: '黎塘'
                         }, {
                             name: 'Zhanjiang'
                         }]
                     ]
                 },
                 geoCoord: {
                     'Alashankou': [82.5757, 45.1706],
                     'Baotou': [109.8403, 40.6574],
                     'Beijing': [116.4075, 39.9040],
                     'Chengdu': [104.0665, 30.5723],
                     'Dalian': [121.6147, 38.9140],
                     'Datong': [113.3001, 40.0768],
                     'Texas': [116.3575, 37.4341],
                     'Fuzhou': [119.2965, 26.0745],
                     'Guangzhou': [113.2644, 23.1292],
                     'Guiyang': [106.6302, 26.6477],
                     'Harbin': [126.5363, 45.8023],
                     'Handan': [114.5391, 36.6256],
                     'Hangzhou': [120.1551, 30.2741],
                     'hefei': [117.2272, 31.8206],
                     '侯马': [111.3720, 35.6191],
                     'Huaihua': [109.9985, 27.5550],
                     'Huaian': [119.0153, 33.6104],
                     '黄骅': [117.3300, 38.3714],
                     'Jinan': [117.1205, 36.6510],
                     'Jiaozuo': [113.2418, 35.2159],
                     'Jiujiang': [116.0019, 29.7051],
                     '九龙红磡': [114.1870, 22.3076],
                     'Kunming': [102.8329, 24.8801],
                     'Lhasa': [91.1409, 29.6456],
                     'Lanzhou': [103.8343, 36.0611],
                     '黎塘': [109.1363, 23.2066],
                     'Lianyungang': [119.2216, 34.5967],
                     'Linfen': [111.5190, 36.0880],
                     'Liuzhou ': [109.4160, 24.3255],
                     '龙口': [120.4778, 37.6461],
                     'Luoyang': [112.4540, 34.6197],
                     '满洲里': [117.3787, 49.5978],
                     'Nanchang': [115.8581, 28.6832],
                     'Nanjing': [118.7969, 32.0603],
                     'Nanning': [108.3661, 22.8172],
                     '南阳': [112.5283, 32.9908],
                     'ningbo': [121.5440, 29.8683],
                     '启东': [121.6574, 31.8082],
                     'qinghuangdao': [119.6005, 39.9354],
                     'Qingdao': [120.3826, 36.0671],
                     'Rizhao': [119.5269, 35.4164],
                     'Xiamen': [118.0894, 24.4798],
                     'Shanghai': [121.4737, 31.2304],
                     'Shenzhen': [114.0579, 22.5431],
                     '神木': [110.4871, 38.8610],
                     'Shenyang': [123.4315, 41.8057],
                     '台前': [115.8717, 35.9701],
                     'Taiyuan': [112.5489, 37.8706],
                     '汤阴': [114.3572, 35.9218],
                     'Tianjin': [117.2010, 39.0842],
                     '铜陵': [117.8121, 30.9454],
                     '瓦塘': [109.7600, 23.3161],
                     'Wenzhou': [120.6994, 27.9943],
                     'Urumqi': [87.6168, 43.8256],
                     'wuhan': [114.3054, 30.5931],
                     'Xian': [108.9402, 34.3416],
                     '新乡': [113.9268, 35.3030],
                     '信阳': [114.0913, 32.1470],
                     'Yantai': [121.4479, 37.4638],
                     '兖州': [116.7838, 35.5531],
                     '月山': [113.0550, 35.2104],
                     'Zhanjiang': [110.3594, 21.2707],
                     'Changzh': [113.1163, 36.1954],
                     'Zhengzhou': [113.6254, 34.7466],
                     'Chongqing': [106.5516, 29.5630]
                 }
             }
         ]
     };

     myChart.setOption(option);
    }
    function echart_6() {
            var myChart = echarts.init(document.getElementById('chart_6'));
                myChart.setOption({
                    series: [{
                        type: 'map',
                        mapType: 'hunan'
                    }]
                });

                var geoCoordMap = {
                    'Huaihua': [109.999867,27.518949],
                    'jishou': [109.741528,28.332629],
                    'zhangjiajie': [110.491722,29.112001],
                    'Changde': [111.701486,29.076683],
                    'Yiyang': [112.348741,28.544124],
                    'Yueyang': [113.126486,29.382401],
                    'Changsha': [113.019455,28.200103],
                    'Zhuzhou': [113.163141,27.8418],
                    'Xiangtan': [112.91977,27.882141],
                    'Shaoyang': [111.467859,27.21915],
                    'Loudi': [112.012438,27.745506],
                    'Hengyang': [112.63809,26.895225],
                    'Yongzhou': [111.577632,26.460144],
                    'Chenzhou': [113.039396,25.81497]
                };

                var goData = [
                    [{
                        name: 'Huaihua'

                    }, {
                        id: 1,
                        name: 'jishou',
                        value: 60
                    }],
                    [{
                        name: 'jishou'

                    }, {
                        id: 1,
                        name: 'zhangjiajie',
                        value: 70
                    }],
                    [{
                        name: 'zhangjiajie'

                    }, {
                        id: 1,
                        name: 'Changde',
                        value: 77
                    }],
                    [{
                        name: 'Changde'

                    }, {
                        id: 1,
                        name: 'Yueyang',
                        value: 70
                    }],
                    [{
                        name: 'Changde'

                    }, {
                        id: 1,
                        name: 'Yiyang',
                        value: 65
                    }],
                    [{
                        name: 'Changde'

                    }, {
                        id: 1,
                        name: 'Shaoyang',
                        value: 80
                    }],
                    [{
                        name: 'Yiyang'

                    }, {
                        id: 1,
                        name: 'Changsha',
                        value: 95
                    }],
                    [{
                        name: 'Yiyang'

                    }, {
                        id: 1,
                        name: 'Loudi',
                        value: 72
                    }],
                    [{
                        name: 'Changsha'

                    }, {
                        id: 1,
                        name: 'Zhuzhou',
                        value: 80
                    }],
                    [{
                        name: 'Changsha'

                    }, {
                        id: 1,
                        name: 'Xiangtan',
                        value: 90
                    }],
                    [{
                        name: 'Changsha'

                    }, {
                        id: 1,
                        name: 'Hengyang',
                        value: 88
                    }],
                    [{
                        name: 'Xiangtan'

                    }, {
                        id: 1,
                        name: 'Loudi',
                        value: 72
                    }],
                    [{
                        name: 'Loudi'

                    }, {
                        id: 1,
                        name: 'Huaihua',
                        value: 80
                    }],
                    [{
                        name: 'Shaoyang'

                    }, {
                        id: 1,
                        name: 'Yongzhou',
                        value: 74
                    }],
                    [{
                        name: 'Hengyang'

                    }, {
                        id: 1,
                        name: 'Shaoyang',
                        value: 80
                    }],
                    [{
                        name: 'Hengyang'

                    }, {
                        id: 1,
                        name: 'Yongzhou',
                        value: 74
                    }],
                    [{
                        name: 'Hengyang'

                    }, {
                        id: 1,
                        name: 'Chenzhou',
                        value: 70
                    }],
                ];
                var backData = [
                    [{
                        name: 'jishou'
                    }, {
                        id: 2,
                        name: 'Huaihua',
                        value: 80
                    }],
                    [{
                        name: 'Changde'

                    }, {
                        id: 1,
                        name: 'zhangjiajie',
                        value: 70
                    }],
                    [{
                        name: 'Yueyang'

                    }, {
                        id: 1,
                        name: 'Changde',
                        value: 77
                    }],
                    [{
                        name: 'Yiyang'

                    }, {
                        id: 1,
                        name: 'Changde',
                        value: 77
                    }],
                    [{
                        name: 'Shaoyang'

                    }, {
                        id: 1,
                        name: 'Changde',
                        value: 77
                    }],
                    [{
                        name: 'Changsha'

                    }, {
                        id: 1,
                        name: 'Yiyang',
                        value: 65
                    }],
                    [{
                        name: 'Loudi'

                    }, {
                        id: 1,
                        name: 'Yiyang',
                        value: 65
                    }],
                    [{
                        name: 'Zhuzhou'

                    }, {
                        id: 1,
                        name: 'Changsha',
                        value: 95
                    }],
                    [{
                        name: 'Xiangtan'

                    }, {
                        id: 1,
                        name: 'Changsha',
                        value: 95
                    }],
                    [{
                        name: 'Hengyang'

                    }, {
                        id: 1,
                        name: 'Changsha',
                        value: 95
                    }],
                    [{
                        name: 'Loudi'

                    }, {
                        id: 1,
                        name: 'Xiangtan',
                        value: 90
                    }],
                    [{
                        name: 'Huaihua'

                    }, {
                        id: 1,
                        name: 'Loudi',
                        value: 72
                    }],
                    [{
                        name: 'Yongzhou'

                    }, {
                        id: 1,
                        name: 'Shaoyang',
                        value: 80
                    }],
                    [{
                        name: 'Shaoyang'

                    }, {
                        id: 1,
                        name: 'Hengyang',
                        value: 88
                    }],
                    [{
                        name: 'Yongzhou'

                    }, {
                        id: 1,
                        name: 'Hengyang',
                        value: 88
                    }],
                    [{
                        name: 'Chenzhou'

                    }, {
                        id: 1,
                        name: 'Hengyang',
                        value: 88
                    }],
                ];

                var arcAngle = function(data) {
                    var j, k;
                    for (var i = 0; i < data.length; i++) {
                        var dataItem = data[i];
                        if (dataItem[1].id == 1) {
                            j = 0.2;
                            return j;
                        } else if (dataItem[1].id == 2) {
                            k = -0.2;
                            return k;
                        }
                    }
                }

                var convertData = function(data) {
                    var res = [];
                    for (var i = 0; i < data.length; i++) {
                        var dataItem = data[i];
                        var fromCoord = geoCoordMap[dataItem[0].name];
                        var toCoord = geoCoordMap[dataItem[1].name];
                        if (dataItem[1].id == 1) {
                            if (fromCoord && toCoord) {
                                res.push([{
                                    coord: fromCoord,
                                }, {
                                    coord: toCoord,
                                    value: dataItem[1].value
                                }]);
                            }
                        } else if (dataItem[1].id == 2) {
                            if (fromCoord && toCoord) {
                                res.push([{
                                    coord: fromCoord,
                                }, {
                                    coord: toCoord
                                }]);
                            }
                        }
                    }
                    return res;
                };

                var color = ['#fff', '#FF1493', '#00FF00'];
                var series = [];
                [
                    ['1', goData],
                    ['2', backData]
                ].forEach(function(item, i) {
                    series.push({
                        name: item[0],
                        type: 'lines',
                        zlevel: 2,
                        symbol: ['arrow', 'arrow'],
                        effect: {
                            show: true,
                            period: 6,
                            trailLength: 0.1,
                            symbol: 'arrow',
                            symbolSize: 5
                        },
                        lineStyle: {
                            normal: {
                                width: 1,
                                opacity: 0.4,
                                curveness: arcAngle(item[1]),
                                color: '#fff'
                            }
                        },
                        data: convertData(item[1])
                    }, {
                        type: 'effectScatter',
                        coordinateSystem: 'geo',
                        zlevel: 2,
                        rippleEffect: {
                            period: 2,
                            brushType: 'stroke',
                            scale: 3
                        },
                        label: {
                            normal: {
                                show: true,
                                color: '#fff',
                                position: 'right',
                                formatter: '{b}'
                            }
                        },
                        symbol: 'circle',
                        symbolSize: function(val) {
                            return val[2] / 8;
                        },
                        itemStyle: {
                            normal: {
                                show: true
                            }
                        },
                        data: item[1].map(function(dataItem) {
                            return {
                                name: dataItem[1].name,
                                value: geoCoordMap[dataItem[1].name].concat([dataItem[1].value])
                            };
                        })

                    });

                });

                option = {
                    title: {
                        text: '',
                        subtext: '',
                        left: 'center',
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: "{b}"
                    },
                    visualMap: {
                        show: false,
                        min: 0,
                        max: 100,
                        color: ['#fff']
                    },
                    geo: {
                        map: 'hunan',
                        zoom: 1,
                        label: {
                            normal: {
                                show: false,
                                textStyle: {
                                    color: '#fff'
                                }
                            },
                            emphasis: {
                                textStyle: {
                                    color: '#fff'
                                }
                            }
                        },
                        roam: true,
                        itemStyle: {
                            normal: {
                                //          	color: '#ddd',
                                borderColor: 'rgba(147, 235, 248, 1)',
                                borderWidth: 1,
                                areaColor: {
                                    type: 'radial',
                                    x: 0.5,
                                    y: 0.5,
                                    r: 0.8,
                                    colorStops: [{
                                        offset: 0,
                                        color: 'rgba(175,238,238, 0)'
                                    }, {
                                        offset: 1,
                                        color: 'rgba(	47,79,79, .2)'
                                    }],
                                    globalCoord: false
                                },
                                shadowColor: 'rgba(128, 217, 248, 1)',
                                shadowOffsetX: -2,
                                shadowOffsetY: 2,
                                shadowBlur: 10
                            },
                            emphasis: {
                                areaColor: '#389BB7',
                                borderWidth: 0
                            }
                        }
                    },
                    series: series
                };
                myChart.setOption(option);
    }
    function echart_7() {
        var myChart = echarts.init(document.getElementById('chart_7'));
        myChart.clear();
        option = {
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data:['the volume of freight transport','Railway freight volume','National railway freight volume','Local railway freight volume',
                    'Freight volume of joint venture railway','Highway freight volume','Water freight volume'],
                textStyle:{
                    color: '#fff'
                },
                top: '4%'
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            toolbox: {
                orient: 'vertical',
                right: '1%',
                top: '2%',
                iconStyle: {
                    color: '#FFEA51',
                    borderColor: '#FFA74D',
                    borderWidth: 1,
                },
                feature: {
                    saveAsImage: {},
                    magicType: {
                        show: true,
                        type: ['line','bar','stack','tiled']
                    }
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['2016','2017','2018','2019','2020'],
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: {
                name: '10000 tons',
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            color: ['#FF4949','#FFA74D','#FFEA51','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1'],
            series: [
                {
                    name:'the volume of freight transport',
                    type:'line',
                    data:[219130, 198009, 209946, 198024, 210586]
                },
                {
                    name:'Railway freight volume',
                    type:'line',
                    data:[21010, 22469, 20619, 17843, 16313]
                },
                {
                    name:'National railway freight volume',
                    type:'line',
                    data:[17866, 19354, 17589, 17709, 18589]
                },
                {
                    name:'Local railway freight volume',
                    type:'line',
                    data:[3034, 2845, 2712, 2790, 2812]
                },
                {
                    name:'Freight volume of joint venture railway',
                    type:'line',
                    data:[111, 271, 318, 327, 349]
                },
                {
                    name:'Highway freight volume',
                    type:'line',
                    data:[195530, 172492, 185286,175637,189822]
                },
                {
                    name:'Water freight volume',
                    type:'line',
                    data:[2590, 3048, 4041,4544,4451]
                }
            ]
        };
        myChart.setOption(option);
    }
    function echart_8() {
        var myChart = echarts.init(document.getElementById('chart_8'));
        myChart.clear();
        option = {
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data:['Railway freight turnover','National railway freight turnover','Local railway freight turnover',
                    'Freight turnover volume of joint venture railway','Highway freight turnover','Turnover volume of water transport goods'],
                textStyle:{
                    color: '#fff'
                },
                top: '4%'
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            toolbox: {
                orient: 'vertical',
                right: '1%',
                top: '2%',
                iconStyle: {
                    color: '#FFEA51',
                    borderColor: '#FFA74D',
                    borderWidth: 1,
                },
                feature: {
                    saveAsImage: {},
                    magicType: {
                        show: true,
                        type: ['line','bar','stack','tiled']
                    }
                }
            },
            color: ['#FF4949','#FFA74D','#FFEA51','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1'],
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['2018','2019','2020','2021','2022'],
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: {
                name: 'Ton kilometers',
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            series: [
                {
                    name:'freight',
                    type:'line',
                    data:[3961.88, 4233.63, 4183.14, 3633.01, 3704.47]
                },
                {
                    name:'National railway freight turnover',
                    type:'line',
                    data:[3374.76, 3364.76, 3274.76, 3371.82, 3259.87]
                },
                {
                    name:'Local railway freight turnover',
                    type:'line',
                    data:[14.77, 15.17, 13.17, 14.56, 15.84]
                },
                {
                    name:'Freight turnover volume of joint venture railway',
                    type:'line',
                    data:[686.17,847.26,895.22,865.28,886.72]
                },
                {
                    name:'Highway freight turnover',
                    type:'line',
                    data:[6133.47, 6577.89, 7019.56,6821.48,7294.59]
                },
                {
                    name:'Turnover volume of water transport goods',
                    type:'line',
                    data:[509.60, 862.54, 1481.77,1552.79,1333.62]
                }
            ]
        };
        myChart.setOption(option);
    }
    function echart_9() {
        var myChart = echarts.init(document.getElementById('chart_9'));
        myChart.clear();
        option = {
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data:['Railway operating mileage','Highway mileage','Class highway mileage','Expressway mileage','Mileage of first-class highways','Mileage of Class II highways','Extraordinary highway mileage'],
                textStyle:{
                    color: '#fff'
                },
                top: '4%'
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            toolbox: {
                orient: 'vertical',
                right: '1%',
                top: '2%',
                iconStyle: {
                    color: '#FFEA51',
                    borderColor: '#FFA74D',
                    borderWidth: 1,
                },
                feature: {
                    saveAsImage: {},
                    magicType: {
                        show: true,
                        type: ['line','bar','stack','tiled']
                    }
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['2018','2019','2020','2021','2022'],
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: {
                name: '10000 kilometers',
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            color: ['#FF4949','#FFA74D','#FFEA51','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1'],
            series: [
                {
                    name:'Railway operating mileage',
                    type:'line',
                    data:[0.56, 0.63, 0.63, 0.70, 0.70]
                },
                {
                    name:'Highway mileage',
                    type:'line',
                    data:[16.30, 17.45, 17.92, 18.46, 18.84]
                },
                {
                    name:'Class highway mileage',
                    type:'line',
                    data:[15.54, 16.77, 17.29, 17.86, 18.26]
                },
                {
                    name:'Expressway mileage',
                    type:'line',
                    data:[0.51, 0.56, 0.59, 0.63, 0.65]
                },
                {
                    name:'Mileage of first-class highways',
                    type:'line',
                    data:[0.47,0.48,0.51,0.54,0.56]
                },
                {
                    name:'Mileage of Class II highways',
                    type:'line',
                    data:[1.76, 1.85, 1.93, 1.97, 1.99]
                },
                {
                    name:'Extraordinary highway mileage',
                    type:'line',
                    data:[0.76, 0.68, 0.63, 0.60, 0.58]
                }
            ]
        };
        myChart.setOption(option);
    }
    function echart_10(){
        var myChart = echarts.init(document.getElementById('chart_10'));
        myChart.clear();

        option = {
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                x: 'left',
                top: '2%',
                left: '1%',
                textStyle: {
                    color: '#fff'
                },
                data:[
                      'international','Outside the province','Province',
                     ]
            },
            color: ['#FF4949','#FFA74D','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1','#4BF0FF','#44AFF0'],
            series: [
                {
                    name:'Business volume',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '15%'],
                    center: ['28%','28%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:90392.39, name:'2022(90392.39)'},
                    ]
                },
                {
                    name:'Business volume',
                    type:'pie',
                    radius: ['20%', '30%'],
                    center: ['28%','28%'],
                    label: {
                        normal: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                    data:[
                        {value:464.43, name:'international'},
                        {value:68575.6, name:'Outside the province'},
                        {value:21352.36, name:'Province'},
                    ]
                },
                {
                    name:'Business volume',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '15%'],
                    center: ['70%','28%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:54911.94, name:'2021(54911.94)'},
                    ]
                },
                {
                    name:'Business volume',
                    type:'pie',
                    radius: ['20%', '30%'],
                    center: ['70%','28%'],
                    label: {
                        normal: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                    data:[
                        {value:278.5, name:'international'},
                        {value:37111.03, name:'Outside the province'},
                        {value:17522.41, name:'Province'},
                    ]
                },
                {
                    name:'Business volume',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '15%'],
                    center: ['28%','70%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:34019.15, name:'2020(34019.15)'},
                    ]
                },
                {
                    name:'Business volume',
                    type:'pie',
                    radius: ['20%', '30%'],
                    center: ['28%','70%'],
                    label: {
                        normal: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                    data:[
                        {value:163.72, name:'international'},
                        {value:26841.29, name:'Outside the province'},
                        {value:7014.14, name:'Province'},
                    ]
                },
                {
                    name:'Business volume',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '15%'],
                    center: ['70%','70%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:20755.74, name:'2019(20755.74)'},
                    ]
                },
                {
                    name:'Business volume',
                    type:'pie',
                    radius: ['20%', '30%'],
                    center: ['70%','70%'],
                    label: {
                        normal: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                    data:[
                        {value:129.65, name:'international'},
                        {value:18072.54, name:'Outside the province'},
                        {value:2553.55, name:'Province'},
                    ]
                },
            ]
        };

        myChart.setOption(option);
    }
    function echart_11(){
        var myChart = echarts.init(document.getElementById('chart_11'));
        myChart.clear();

        option = {
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                x: 'left',
                top: '2%',
                left: '1%',
                textStyle: {
                    color: '#fff'
                },
                data:['Road operation carrying passengers','Highway operation cargo carrying']
            },
            color: ['#FF4949','#FFA74D','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1'],
            series: [
                {
                    name:'公路营运',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '15%'],
                    center: ['28%','28%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:145.18, name:'2022(145.18)'},
                    ]
                },
                {
                    name:'Car ownership',
                    type:'pie',
                    radius: ['20%', '30%'],
                    center: ['28%','28%'],
                    label: {
                        normal: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            position: 'outside',
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                
                    data:[
                        {value:142.65, name:'Road operation carrying passengers'},
                        {value:2.53, name:'Highway operation cargo carrying'},
                    ]
                },
                {
                    name:'公路营运',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '15%'],
                    center: ['70%','28%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:142.47, name:'2021(142.47)'}
                    ]
                },
                {
                    name:'Car ownership',
                    type:'pie',
                    radius: ['20%', '30%'],
                    center: ['70%','28%'],
                    label: {
                        normal: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            position: 'outside',
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                
                    data:[
                        {value:139.95, name:'Road operation carrying passengers'},
                        {value:2.52, name:'Highway operation cargo carrying'},
                    ]
                },
                {
                    name:'公路营运',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '15%'],
                    center: ['28%','70%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:140.61, name:'2020(140.61)'},
                    ]
                },
                {
                    name:'Car ownership',
                    type:'pie',
                    radius: ['20%', '30%'],
                    center: ['28%','70%'],
                    label: {
                        normal: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            position: 'outside',
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                
                    data:[
                        {value:137.96, name:'Road operation carrying passengers'},
                        {value:2.65, name:'Highway operation cargo carrying'},
                    ]
                },
                {
                    name:'公路营运',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '15%'],
                    center: ['70%','70%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:134.45, name:'2019(134.45)'},
                    ]
                },
                {
                    name:'Car ownership',
                    type:'pie',
                    radius: ['20%', '30%'],
                    center: ['70%','70%'],
                    label: {
                        normal: {
                            formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                            backgroundColor: '#eee',
                            borderColor: '#aaa',
                            borderWidth: 1,
                            borderRadius: 4,
                            position: 'outside',
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                
                    data:[
                        {value:131.48, name:'Road operation carrying passengers'},
                        {value:2.97, name:'Highway operation cargo carrying'},
                    ]
                }
            ]
        };

        myChart.setOption(option);
    }
    function echart_12() {
        var myChart = echarts.init(document.getElementById('chart_12'));
        myChart.clear();
        option = {
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data:['Number of public transportation operations','Total length of operating lines','Total passenger volume of public transportation'],
                textStyle:{
                    color: '#fff'
                },
                top: '4%'
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            toolbox: {
                orient: 'vertical',
                right: '1%',
                top: '2%',
                iconStyle: {
                    color: '#FFEA51',
                    borderColor: '#FFA74D',
                    borderWidth: 1,
                },
                feature: {
                    saveAsImage: {},
                    magicType: {
                        show: true,
                        type: ['line','bar','stack','tiled']
                    }
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['2018','2019','2020','2021','2022'],
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: {
                name: '10000 kilometers',
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            color: ['#FF4949','#FFA74D','#FFEA51','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1'],
            series: [
                {
                    name:'Number of public transportation operations',
                    type:'line',
                    data:[16493,17498, 15977, 18927, 21479]
                },
                {
                    name:'Total length of operating lines',
                    type:'line',
                    data:[18812, 19647, 20305, 22940, 26077]
                },
                {
                    name:'Total passenger volume of public transportation',
                    type:'line',
                    data:[203954, 202727, 205342, 187208, 186048]
                },
            ]
        };
        myChart.setOption(option);
    }
    function echart_13(){
        var myChart = echarts.init(document.getElementById('chart_13'));
        function showProvince() {
                myChart.setOption(option = {
                    // backgroundColor: '#ffffff',
                    visualMap: {
                        show: false,
                        min: 0,
                        max: 100,
                        left: 'left',
                        top: 'bottom',
                        text: ['高', '低'],
                        calculable: true,
                        inRange: {
                            color: ['yellow', 'lightskyblue', 'orangered']
                        }
                    },
                    series: [{
                        type: 'map',
                        mapType: 'hunan',
                        roam: true,
                        label: {
                            normal: {
                                show: true
                            },
                            emphasis: {
                                textStyle: {
                                    color: '#fff'
                                }
                            }
                        },
                        itemStyle: {
                            normal: {
                                borderColor: '#389BB7',
                                areaColor: '#fff',
                            },
                            emphasis: {
                                areaColor: '#389BB7',
                                borderWidth: 0
                            }
                        },
                        animation: false,
                        data: [{
                            name: 'Changsha City',
                            value:  100
                        }, {
                            name: 'Zhuzhou City',
                            value: 96
                        }, {
                            name: 'Xiangtan City',
                            value: 98
                        }, {
                            name: 'Hengyang City',
                            value: 80
                        }, {
                            name: 'Shaoyang City',
                            value: 88
                        }, {
                            name: 'Yueyang City',
                            value: 79
                        }, {
                            name: 'Changde City',
                            value: 77,
                        }, {
                            name: 'Zhangjiajie City',
                            value: 33
                        }, {
                            name: 'Yiyang City',
                            value: 69,
                        }, {
                            name: 'Chenzhou City',
                            value: 66
                        }, {
                            name: 'Yongzhou City',
                            value: 22
                        },{
                            name: 'Loudi City',
                            value: 51
                        },{
                            name: 'Xiangxi Tujia and Miao Autonomous Prefecture',
                            value: 44
                        },{
                            name: 'Huaihua city',
                            value: 9
                        }]
                    }]
                });
        }

        var currentIdx = 0;
        showProvince();
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
    //GPS
    function echart_14(){
        var myChart = echarts.init(document.getElementById('chart_14'));

        var data = [
             {name: 'Haimen', value: 9,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'erdos', value: 12,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhaoyuan', value: 12,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhoushan', value: 12,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Qiqihar', value: 14,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: ' Yencheng ', value: 15,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Chifeng', value: 16,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Qingdao', value: 18,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Rushan', value: 18,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jinchang', value: 19,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Quanzhou', value: 21,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Laixi', value: 21,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Rizhao', value: 21,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jiaonan', value: 22,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Nantong', value: 23,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Lhasa', value: 24,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yunfu', value: 24,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Meizhou', value: 25,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Wendeng', value: 25,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shanghai', value: 25,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Panzhihua', value: 25,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Weihai', value: 25,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'chengde', value: 25,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Xiamen', value: 26,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shanwei', value: 26,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Chaozhou', value: 26,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Dandong', value: 27,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Taicang', value: 27,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Qujing', value: 27,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yantai', value: 28,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Fuzhou', value: 29,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Wafangdian', value: 30,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jimo ', value: 30,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Fushun', value: 31,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yuxi', value: 31,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhangjiakou', value: 31,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yangquan', value: 31,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'laizhou', value: 32,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'huzhou', value: 32,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'shantou', value: 32,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'kunsan', value: 33,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'ningbo', value: 33,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhanjiang', value: 33,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jieyang ', value: 34,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Rongcheng', value: 34,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Lianyungang', value: 35,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Huludao', value: 35,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Changshu', value: 36,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Dongguan', value: 36,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Heyuan', value: 36,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Huaian', value: 36,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Taizhou1', value: 36,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Nanning', value: 37,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yingkou', value: 37,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Huizhou', value: 37,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jiangyin', value: 37,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Penglai', value: 37,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shaoguan', value: 38,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jiayuguan', value: 38,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Guangzhou', value: 38,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yanan', value: 38,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Taiyuan', value: 39,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Qingyuan', value: 39,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhongshan', value: 39,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Kunming', value: 39,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shouguang', value: 40,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Panjin', value: 40,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Changzh', value: 41,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shenzhen', value: 41,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhuhai', value: 42,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Suqian', value: 43,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Xianyang', value: 43,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Tongchuan', value: 44,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Pingdu', value: 44,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Foshan', value: 44,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Haikou', value: 44,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jiangmen', value: 45,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhangqiu', value: 45,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhaoqing', value: 46,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Dalian', value: 47,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Linfen', value: 47,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Wujiang', value: 47,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shizuishan', value: 49,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shenyang', value: 50,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Suzhou', value: 50,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Maoming', value: 50,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jiaxing', value: 51,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Changchun', value: 51,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jiaozhou', value: 52,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yinchuan', value: 52,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhangjiagang', value: 52,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Sanmenxia', value: 53,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jinzhou', value: 54,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Nanchang', value: 54,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Liuzhou ', value: 54,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Sanya', value: 54,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zigong', value: 56,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jilin', value: 56,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yangjiang', value: 57,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Luzhou', value: 57,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Xining', value: 57,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yibin', value: 58,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Hohhot', value: 58,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Chengdu', value: 58,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Datong', value: 58,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhenjiang', value: 59,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Guilin', value: 59,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhangjiajie', value: 59,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yixing', value: 59,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Beihai ', value: 60,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Xian', value: 61,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jintan', value: 62,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Dongying ', value: 62,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Mudanjiang', value: 63,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zunyi', value: 63,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shaoxing', value: 63,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yangzhou', value: 64,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Changzhou', value: 64,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Weifang', value: 65,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Chongqing', value: 66,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Taizhou', value: 67,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Nanjing', value: 67,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Binzhou', value: 70,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Guiyang', value: 71,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Wuxi', value: 71,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Benxi', value: 71,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Karamay', value: 72,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Weinan', value: 72,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'MaAnshan', value: 72,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Baoji', value: 72,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jiaozuo', value: 75,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'jurong', value: 75,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Beijing', value: 79,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Xuzhou', value: 79,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Hengshui', value: 80,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Baotou', value: 80,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Mianyang', value: 80,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Urumqi', value: 84,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zaozhuang', value: 84,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Hangzhou', value: 84,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zibo', value: 85,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Anshan', value: 86,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Liyang', value: 86,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Korla', value: 86,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Anyang ', value: 90,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Kaifeng ', value: 90,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jinan', value: 92,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Deyang', value: 93,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Wenzhou', value: 95,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jiujiang', value: 96,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Handan', value: 98,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Linan', value: 99,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Lanzhou', value: 99,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Cangzhou', value: 100,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Linyi', value: 103,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Nanchong', value: 104,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Tianjin', value: 105,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Fuyang', value: 106,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Taian', value: 112,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhuji', value: 112,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhengzhou', value: 113,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Harbin', value: 114,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Liaocheng', value: 116,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Wuhu', value: 117,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Tangshan', value: 119,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Pingdingshan', value: 119,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Xingtai', value: 119,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Texas', value: 120,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jining', value: 120,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jingzhou', value: 127,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yichang', value: 130,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Yiwu', value: 132,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Lishui', value: 133,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Luoyang', value: 134,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'qinghuangdao', value: 136,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Zhuzhou', value: 143,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Shijiazhuang', value: 147,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Laiwu', value: 148,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'changde', value: 152,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Baoding', value: 153,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Xiangtan', value: 154,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Jinhua', value: 157,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'yueyang', value: 169,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Changsha', value: 175,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Quzhou', value: 177,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Langfang', value: 170,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'Heze', value: 175,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {name: 'hefei', value: 180,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'},
             {
                name: 'wuhan',
                value: 190,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'
            },
            {
                name: 'Daqing ',
                value: 150,
                address:'2038 East Huanyu Road, Erdao District',
                typeName:'combined transport',
                area:'0.18',
                service:'Northeast region'
            }
        ];
        var geoCoordMap = {
            'Haimen':[121.15,31.89],
            'erdos':[109.781327,39.608266],
            'Zhaoyuan':[120.38,37.35],
            'Zhoushan':[122.207216,29.985295],
            'Qiqihar':[123.97,47.33],
            ' Yencheng ':[120.13,33.38],
            'Chifeng':[118.87,42.28],
            'Qingdao':[120.33,36.07],
            'Rushan':[121.52,36.89],
            'Jinchang':[102.188043,38.520089],
            'Quanzhou':[118.58,24.93],
            'Laixi':[120.53,36.86],
            'Rizhao':[119.46,35.42],
            'Jiaonan':[119.97,35.88],
            'Nantong':[121.05,32.08],
            'Lhasa':[91.11,29.97],
            'Yunfu':[112.02,22.93],
            'Meizhou':[116.1,24.55],
            'Wendeng':[122.05,37.2],
            'Shanghai':[121.48,31.22],
            'Panzhihua':[101.718637,26.582347],
            'Weihai':[122.1,37.5],
            'chengde':[117.93,40.97],
            'Xiamen':[118.1,24.46],
            'Shanwei':[115.375279,22.786211],
            'Chaozhou':[116.63,23.68],
            'Dandong':[124.37,40.13],
            'Taicang':[121.1,31.45],
            'Qujing':[103.79,25.51],
            'Yantai':[121.39,37.52],
            'Fuzhou':[119.3,26.08],
            'Wafangdian':[121.979603,39.627114],
            'Jimo ':[120.45,36.38],
            'Fushun':[123.97,41.97],
            'Yuxi':[102.52,24.35],
            'Zhangjiakou':[114.87,40.82],
            'Yangquan':[113.57,37.85],
            'laizhou':[119.942327,37.177017],
            'huzhou':[120.1,30.86],
            'shantou':[116.69,23.39],
            'kunsan':[120.95,31.39],
            'ningbo':[121.56,29.86],
            'Zhanjiang':[110.359377,21.270708],
            'Jieyang ':[116.35,23.55],
            'Rongcheng':[122.41,37.16],
            'Lianyungang':[119.16,34.59],
            'Huludao':[120.836932,40.711052],
            'Changshu':[120.74,31.64],
            'Dongguan':[113.75,23.04],
            'Heyuan':[114.68,23.73],
            'Huaian':[119.15,33.5],
            'Taizhou1':[119.9,32.49],
            'Nanning':[108.33,22.84],
            'Yingkou':[122.18,40.65],
            'Huizhou':[114.4,23.09],
            'Jiangyin':[120.26,31.91],
            'Penglai':[120.75,37.8],
            'Shaoguan':[113.62,24.84],
            'Jiayuguan':[98.289152,39.77313],
            'Guangzhou':[113.23,23.16],
            'Yanan':[109.47,36.6],
            'Taiyuan':[112.53,37.87],
            'Qingyuan':[113.01,23.7],
            'Zhongshan':[113.38,22.52],
            'Kunming':[102.73,25.04],
            'Shouguang':[118.73,36.86],
            'Panjin':[122.070714,41.119997],
            'Changzh':[113.08,36.18],
            'Shenzhen':[114.07,22.62],
            'Zhuhai':[113.52,22.3],
            'Suqian':[118.3,33.96],
            'Xianyang':[108.72,34.36],
            'Tongchuan':[109.11,35.09],
            'Pingdu':[119.97,36.77],
            'Foshan':[113.11,23.05],
            'Haikou':[110.35,20.02],
            'Jiangmen':[113.06,22.61],
            'Zhangqiu':[117.53,36.72],
            'Zhaoqing':[112.44,23.05],
            'Dalian':[121.62,38.92],
            'Linfen':[111.5,36.08],
            'Wujiang':[120.63,31.16],
            'Shizuishan':[106.39,39.04],
            'Shenyang':[123.38,41.8],
            'Suzhou':[120.62,31.32],
            'Maoming':[110.88,21.68],
            'Jiaxing':[120.76,30.77],
            'Changchun':[125.35,43.88],
            'Jiaozhou':[120.03336,36.264622],
            'Yinchuan':[106.27,38.47],
            'Zhangjiagang':[120.555821,31.875428],
            'Sanmenxia':[111.19,34.76],
            'Jinzhou':[121.15,41.13],
            'Nanchang':[115.89,28.68],
            'Liuzhou ':[109.4,24.33],
            'Sanya':[109.511909,18.252847],
            'Zigong':[104.778442,29.33903],
            'Jilin':[126.57,43.87],
            'Yangjiang':[111.95,21.85],
            'Luzhou':[105.39,28.91],
            'Xining':[101.74,36.56],
            'Yibin':[104.56,29.77],
            'Hohhot':[111.65,40.82],
            'Chengdu':[104.06,30.67],
            'Datong':[113.3,40.12],
            'Zhenjiang':[119.44,32.2],
            'Guilin':[110.28,25.29],
            'Zhangjiajie':[110.479191,29.117096],
            'Yixing':[119.82,31.36],
            'Beihai ':[109.12,21.49],
            'Xian':[108.95,34.27],
            'Jintan':[119.56,31.74],
            'Dongying ':[118.49,37.46],
            'Mudanjiang':[129.58,44.6],
            'Zunyi':[106.9,27.7],
            'Shaoxing':[120.58,30.01],
            'Yangzhou':[119.42,32.39],
            'Changzhou':[119.95,31.79],
            'Weifang':[119.1,36.62],
            'Chongqing':[106.54,29.59],
            'Taizhou':[121.420757,28.656386],
            'Nanjing':[118.78,32.04],
            'Binzhou':[118.03,37.36],
            'Guiyang':[106.71,26.57],
            'Wuxi':[120.29,31.59],
            'Benxi':[123.73,41.3],
            'Karamay':[84.77,45.59],
            'Weinan':[109.5,34.52],
            'MaAnshan':[118.48,31.56],
            'Baoji':[107.15,34.38],
            'Jiaozuo':[113.21,35.24],
            'jurong':[119.16,31.95],
            'Beijing':[116.46,39.92],
            'Xuzhou':[117.2,34.26],
            'Hengshui':[115.72,37.72],
            'Baotou':[110,40.58],
            'Mianyang':[104.73,31.48],
            'Urumqi':[87.68,43.77],
            'Zaozhuang':[117.57,34.86],
            'Hangzhou':[120.19,30.26],
            'Zibo':[118.05,36.78],
            'Anshan':[122.85,41.12],
            'Liyang':[119.48,31.43],
            'Korla':[86.06,41.68],
            'Anyang ':[114.35,36.1],
            'Kaifeng ':[114.35,34.79],
            'Jinan':[117,36.65],
            'Deyang':[104.37,31.13],
            'Wenzhou':[120.65,28.01],
            'Jiujiang':[115.97,29.71],
            'Handan':[114.47,36.6],
            'Linan':[119.72,30.23],
            'Lanzhou':[103.73,36.03],
            'Cangzhou':[116.83,38.33],
            'Linyi':[118.35,35.05],
            'Nanchong':[106.110698,30.837793],
            'Tianjin':[117.2,39.13],
            'Fuyang':[119.95,30.07],
            'Taian':[117.13,36.18],
            'Zhuji':[120.23,29.71],
            'Zhengzhou':[113.65,34.76],
            'Harbin':[126.63,45.75],
            'Liaocheng':[115.97,36.45],
            'Wuhu':[118.38,31.33],
            'Tangshan':[118.02,39.63],
            'Pingdingshan':[113.29,33.75],
            'Xingtai':[114.48,37.05],
            'Texas':[116.29,37.45],
            'Jining':[116.59,35.38],
            'Jingzhou':[112.239741,30.335165],
            'Yichang':[111.3,30.7],
            'Yiwu':[120.06,29.32],
            'Lishui':[119.92,28.45],
            'Luoyang':[112.44,34.7],
            'qinghuangdao':[119.57,39.95],
            'Zhuzhou':[113.16,27.83],
            'Shijiazhuang':[114.48,38.03],
            'Laiwu':[117.67,36.19],
            'changde':[111.69,29.05],
            'Baoding':[115.48,38.85],
            'Xiangtan':[112.91,27.87],
            'Jinhua':[119.64,29.12],
            'yueyang':[113.09,29.37],
            'Changsha':[113,28.21],
            'Quzhou':[118.88,28.97],
            'Langfang':[116.7,39.53],
            'Heze':[115.480656,35.23375],
            'hefei':[117.27,31.86],
            'wuhan':[114.31,30.52],
            'Daqing ':[125.03,46.58]
        };

        var convertData = function (data) {
            var res = [];
            for (var i = 0; i < data.length; i++) {
                var geoCoord = geoCoordMap[data[i].name];
                if (geoCoord) {
                    res.push({
                        name: data[i].name,
                        value: geoCoord.concat(data[i].value)
                    });
                }

            }
            return res;
        };

        var option = {
            title: {
                text: '',
            },
            tooltip : {
                show: false,
                trigger: 'item',
                formatter: '{b}<br>{c}',
            },
            bmap: {
                center: [104.114129, 37.550339],
                zoom: 5,
                roam: false,
                mapStyle: {
                    styleJson: [{
                        'featureType': 'land',
                        'elementType': 'all',
                        'stylers': {
                            'color': '#f5f3ef'
                        }
                    },{
                        'featureType': 'water',
                        'elementType': 'all',
                        'stylers': {
                            'color': '#a2c1de'
                        }
                    }, {
                        'featureType': 'railway',
                        'elementType': 'all',
                        'stylers': {
                            'visibility': 'off'
                        }
                    }, {
                        'featureType': 'highway',
                        'elementType': 'all',
                        'stylers': {
                            'color': '#fdfdfd'
                        }
                    }, {
                        'featureType': 'highway',
                        'elementType': 'labels',
                        'stylers': {
                            'visibility': 'off'
                        }
                    }, {
                        'featureType': 'arterial',
                        'elementType': 'geometry',
                        'stylers': {
                            'color': '#fefefe'
                        }
                    }, {
                        'featureType': 'arterial',      
                        'elementType': 'geometry.fill',
                        'stylers': {
                            'color': '#fefefe'
                        }
                    }, {
                        'featureType': 'poi',
                        'elementType': 'all',
                        'stylers': {
                            'visibility': 'off'
                        }
                    }, {
                        'featureType': 'green',
                        'elementType': 'all',
                        'stylers': {
                            'visibility': 'off'
                        }
                    }, {
                        'featureType': 'subway',
                        'elementType': 'all',
                        'stylers': {
                            'visibility': 'off'
                        }
                    }, {
                        'featureType': 'manmade',
                        'elementType': 'all',
                        'stylers': {
                            'color': '#d1d1d1'
                        }
                    }, {
                        'featureType': 'local',
                        'elementType': 'all',
                        'stylers': {
                            'color': '#d1d1d1'
                        }
                    }, {
                        'featureType': 'arterial',
                        'elementType': 'labels',
                        'stylers': {
                            'visibility': 'off'
                        }
                    }, {
                        'featureType': 'boundary',
                        'elementType': 'all',
                        'stylers': {
                            'color': '#bcab78'
                        }
                    }, {
                        'featureType': 'building',
                        'elementType': 'all',
                        'stylers': {
                            'color': '#d1d1d1'
                        }
                    }, {
                        'featureType': 'label',
                        'elementType': 'labels.text.fill',
                        'stylers': {
                            'color': '#898989'
                        }
                    }]
                }
            },
            series : [
                {
                    name: 'pm2.5',
                    type: 'scatter',
                    coordinateSystem: 'bmap',
                    data: convertData(data),
                    hoverAnimation: false,
                    symbolSize: function (val) {
                        return val[2] / 10;
                    },
                    label: {
                        normal: {
                            formatter: '{b}',
                            position: 'right',
                            show: false
                        },
                        emphasis: {
                            show: false
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: '#de1300'
                        }
                    }
                }
            ]
        };

        myChart.setOption(option);
        
        var bmap = myChart.getModel().getComponent('bmap').getBMap();
        bmap.addControl(new BMap.NavigationControl());
        bmap.enableDragging();

        var opts = {
                    offset: {height:-5,width:5},
                    width : 250,
                    height: 150,
                    title : "" ,
                    enableMessage:true
                   };
        for(var i=0;i<data.length;i++){
            var icon = new BMap.Icon('../images/ico.png', new BMap.Size(10, 10), {
                anchor: new BMap.Size(5, 5)
            });
            var marker = new BMap.Marker(new BMap.Point(geoCoordMap[data[i].name][0],geoCoordMap[data[i].name][1]),{icon: icon});
            var content = "<b>"+data[i].name+"</b><br><br>" +
                            "Park address："+ data[i].address +"<br>" +
                            "Park type："+ data[i].typeName +"<br>" +
                            "Park area："+ data[i].area +"<br>" +
                            "Settled Enterprise："+ data[i].value +"<br>"+
                            "Service scope："+ data[i].service;

            bmap.addOverlay(marker);
            addClickHandler(content,marker);
        }
        function addClickHandler(content,marker){
            marker.addEventListener("mouseover",function(e){
                openInfo(content,e);
            });
            marker.addEventListener("mouseout",function(e){
                bmap.closeInfoWindow();
            });
        }
        function openInfo(content,e){
            var p = e.target;
            var point = new BMap.Point(p.getPosition().lng, p.getPosition().lat);
            var infoWindow = new BMap.InfoWindow(content,opts);
            bmap.openInfoWindow(infoWindow,point);
        }
    }
    $('.t_btn0').click(function () {
        $('.center_text').css('display', 'none');
        $('.t_cos0').css('display', 'block');
        echart_map();
    });
    $('.t_btn1').click(function () {
        $('.center_text').css('display', 'none');
        $('.t_cos1').css('display', 'block');
        echart_2();
    });
    $('.t_btn2').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos2').css('display', 'block');
        echart_0();
    });
    $('.t_btn3').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos3').css('display', 'block');
        echart_4();
    });
    $('.t_btn4').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos6').css('display', 'block');
        echart_6();
    });
    $('.t_btn5').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos4').css('display', 'block');
        echart_1();
    });
    $('.t_btn6').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos5').css('display', 'block');
        echart_3();
    });
    $('.t_btn7').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos7').css('display', 'block');
        echart_7();
    });
    $('.t_btn8').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos8').css('display', 'block');
        echart_8();
    });
    $('.t_btn9').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos9').css('display', 'block');
        echart_9();
    });
    $('.t_btn10').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos10').css('display', 'block');
        echart_10();
    });
    $('.t_btn11').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos11').css('display', 'block');
        echart_11();
    });
    $('.t_btn12').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos12').css('display', 'block');
        echart_12();
    });
    $('.t_btn13').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos13').css('display', 'block');
        echart_13();
    });
    $('.t_btn14').click(function(){
        $('.center_text').css('display', 'none');
        $('.t_cos14').css('display', 'block');
        echart_14();
    });
    $(function(){
        function getUrlParms(name){
            var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
            var r = window.location.search.substr(1).match(reg);
                if(r!=null)
                return unescape(r[2]);
                return null;
            }
            var id = getUrlParms("id");  
            if(id == 2){
                $('.center_text').css('display', 'none');
                $('.t_cos10').css('display', 'block');
                echart_10();
            }
            if(id == 3){
                $('.center_text').css('display', 'none');
                $('.t_cos11').css('display', 'block');
                echart_11();
            }
            if(id == 4){
                $('.center_text').css('display', 'none');
                $('.t_cos1').css('display', 'block');
                echart_2();
            }
            if(id == 5){
                $('.center_text').css('display', 'none');
                $('.t_cos6').css('display', 'block');
                echart_6();
            }
            if(id == 6){
                $('.center_text').css('display', 'none');
                $('.t_cos4').css('display', 'block');
                echart_1();
            }
            if(id == 7){
                $('.center_text').css('display', 'none');
                $('.t_cos8').css('display', 'block');
                echart_8();
            }
            if(id == 8){
                $('.center_text').css('display', 'none');
                $('.t_cos12').css('display', 'block');
                echart_12();
            }
            if(id == 9){
                $('.center_text').css('display', 'none');
                $('.t_cos13').css('display', 'block');
                echart_13();
            }
    });
});
