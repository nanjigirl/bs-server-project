<template>
  <div id="lineChart" :style="{height: height + 'px'}"></div>
</template>

<script>
    export default {
        props: {
            height: {
                type: Number,
                default: 240
            },
            tableTitle: {
                type: String,
                default: ''
            },
            xData: {
                type: Array,
                default: []
            },
            yData: {
                type: Array,
                default: []
            }
        },
        data () {
            return {
                
            }
        },
        watch: {
            tableTitle() {
                this.initData()
            }
        },
        methods: {
            initData() {
                // 基于准备好的dom，初始化echarts实例
                let myChart = this.$echarts.init(document.getElementById('lineChart'));        

                let that = this

                let options = {
                    color: ['#324157','#c23531'],
                    title: {                        
                        text: that.tableTitle,
                        top:10,
                        left:10
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: "{a} <br/>{b} : {c}次"
                    },
                    toolbox: {
                        show : true,
                        top:10,
                        right:10,
                        feature : {
                            mark : {show: true},
                            magicType : {show: true, type: ['line', 'bar']},
                            restore : {show: true},
                            saveAsImage : {show: true}
                        }
                    },
                    grid:{
                        top:80,
                        right:70,
                        bottom:30,
                        left:60
                    },                    
                    calculable : true,
                    xAxis : [
                        {
                            type : 'category',
                            data : that.xData
                        }
                    ],
                    yAxis: {
                        type: 'value',
                        name:"阴\n极\n保\n护\n电\n位\n︵\nC\nS\nE\n︶",
                        nameLocation:"center",
                        nameGap:35,
                        nameRotate:0,                                                                       
                        nameTextStyle:{
                            fontSize: 16,
                        },
                        //默认以千分位显示，不想用的可以在这加一段
                        axisLabel : {   //调整左侧Y轴刻度， 直接按对应数据显示
                            show:true,
                            showMinLabel:true,
                            showMaxLabel:true,
                            formatter: function (value) {
                                return value;
                            }
                        }
                    },
                    series : that.yData
                };
                if(that.yData.length > 1) {
                    let extraOptions = {
                        legend: {
                            top:32,
                            left:'center',
                            data:['真实值','预测值']
                        }                                               
                    }
                    // 设置y轴最小值为数据最小值
                    options.yAxis.scale = true;
                    // 设置y轴最大值
                    //options.yAxis.max = -0.8;
                    Object.assign(options, extraOptions);                   
                }
                console.log(options);
                // 绘制图表
                myChart.setOption(options);
            }
        },      
        mounted() {   
            this.$nextTick(() => {
              this.initData();
            });
        }
    }
</script>
