$(function () {
    echart_1();
    echart_2();

    echart_3();
    echart_4();

    echart_map();
    echart_5();

    function echart_1() {
        var myChart = echarts.init(document.getElementById('chart_1'));
        option = {
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c}"
            },
            legend: {
                x: 'center',
                y: '15%',
                data: [ 'Zhangjiakou', 'chengde', 'Hengshui','邢台', 'Handan', 'Baoding','qinghuangdao','Shijiazhuang', 'Tangshan'],
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
                radius: [41, 100.75],
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
                        name: 'Zhangjiakou',
                        itemStyle: {
                            normal: {
                                color: '#f845f1'
                            }
                        }
                    },
                    {
                        value: 1100.58,
                        name: 'chengde',
                        itemStyle: {
                            normal: {
                                color: '#ad46f3'
                            }
                        }
                    },
                    {
                        value: 1200.58,
                        name: 'Hengshui',
                        itemStyle: {
                            normal: {
                                color: '#5045f6'
                            }
                        }
                    },
                    {
                        value: 1300.58,
                        name: '邢台',
                        itemStyle: {
                            normal: {
                                color: '#4777f5'
                            }
                        }
                    },
                    {
                        value: 1400.58,
                        name: 'Handan',
                        itemStyle: {
                            normal: {
                                color: '#44aff0'
                            }
                        }
                    },
                    {
                        value: 1500.58,
                        name: 'Baoding',
                        itemStyle: {
                            normal: {
                                color: '#45dbf7'
                            }
                        }
                    },
                    {
                        value: 1500.58,
                        name: 'qinghuangdao',
                        itemStyle: {
                            normal: {
                                color: '#f6d54a'
                            }
                        }
                    },
                    {
                        value: 1600.58,
                        name: 'Shijiazhuang',
                        itemStyle: {
                            normal: {
                                color: '#f69846'
                            }
                        }
                    },
                    {
                        value: 1800,
                        name: 'Tangshan',
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

    function echart_2() {
           var myChart = echarts.init(document.getElementById('chart_2'));
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
            'haikou': [110.3893, 19.8516],
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
                name: 'haikou',
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
                                color: 'rgba(47,79,79, .1)'
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
                data:['railroad cargo','National Railway Freight','Local railway cargo','Joint venture railway freight','Highway cargo','Water cargo'],
                textStyle:{
                    color: '#fff'
                },
                top: '8%'
            },
            grid: {
                top: '40%',
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            color: ['#FF4949','#FFA74D','#FFEA51','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1'],
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
                    name:'railroad cargo',
                    type:'line',
                    data:[3961.88, 4233.63, 4183.14, 3633.01, 3704.47]
                },
                {
                    name:'National Railway Freight',
                    type:'line',
                    data:[3374.76, 3364.76, 3274.76, 3371.82, 3259.87]
                },
                {
                    name:'Local railway cargo',
                    type:'line',
                    data:[14.77, 15.17, 13.17, 14.56, 15.84]
                },
                {
                    name:'Joint venture railway freight',
                    type:'line',
                    data:[686.17,847.26,895.22,865.28,886.72]
                },
                {
                    name:'Highway cargo',
                    type:'line',
                    data:[6133.47, 6577.89, 7019.56,6821.48,7294.59]
                },
                {
                    name:'Water cargo',
                    type:'line',
                    data:[509.60, 862.54, 1481.77,1552.79,1333.62]
                }
            ]
        };
        myChart.setOption(option);
    }
    function echart_4() {
          var myChart = echarts.init(document.getElementById('chart_4'));

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
              'Yiyang': [112.348741,28.544124],
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
                  name: 'Yiyang',
                  value: 70
              }],
              [{
                  name: 'Yiyang'

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
                  name: 'Yiyang'

              }, {
                  id: 1,
                  name: 'changde',
                  value: 86
              }],
              [{
                  name: 'Changsha'

              }, {
                  id: 1,
                  name: 'Yiyang',
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
    function echart_5() {
        var myChart = echarts.init(document.getElementById('chart_5'));

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

        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
    $('#chart_map').click(function(){
        window.location.href = './page/index.html';
    });
    $('.t_btn2').click(function(){
        window.location.href = "./page/index.html?id=2";
    });
    $('.t_btn3').click(function(){
        window.location.href = "./page/index.html?id=3";
    });
    $('.t_btn4').click(function(){
        window.location.href = "./page/index.html?id=4";
    });
    $('.t_btn5').click(function(){
        window.location.href = "./page/index.html?id=5";
    });
    $('.t_btn6').click(function(){
        window.location.href = "./page/index.html?id=6";
    });
    $('.t_btn7').click(function(){
        window.location.href = "./page/index.html?id=7";
    });
    $('.t_btn8').click(function(){
        window.location.href = "./page/index.html?id=8";
    });
    $('.t_btn9').click(function(){
        window.location.href = "./page/index.html?id=9";
    });
});
