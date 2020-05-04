<template>
  <el-row class="wrap">
    <el-col :span="24" class="toolbar" style="padding-bottom:0px;">
      <!--form表单-->
      <el-form :inline="true">
        <el-form-item label="数据类别">
          <el-select v-model="form.region" placeholder="--请选择--" @change="handleTableName">
            <!-- <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option> -->
            <el-option v-for="(item, i) in dataType" :key="i" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="时间区间">
          <el-col :span="11">
            <el-date-picker
              type="datetime"
              format = "yyyy-MM-dd HH:mm"
              placeholder="选择日期"
              v-model="form.date1"
              style="width: 100%;"
            ></el-date-picker>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-date-picker
              type="datetime"
              format = "yyyy-MM-dd HH:mm"
              placeholder="选择日期"
              v-model="form.date2"
              style="width: 100%;"
            ></el-date-picker>
          </el-col>
        </el-form-item>
      </el-form>

      <!--折线图-->
      <line-chart :table-title="title" :height="400" :xData="xData" :yData="yData"></line-chart>            
    </el-col>
  </el-row>
</template>

<script>
import LineChart from "./ChartApi/LineChart.vue";
// let { xData, yData } = require("./../mock/DataManager.json");
export default {
  data() {
    return {
      //form控件
      dataType: [
        {
          label: '通电电位',
          value: 'cp',
        },
        {
          label: '阴极保护电位',
          value: 'pop',
        },
        {
          label: '自腐蚀电位',
          value: 'np',
        },
        {
          label: '交流AK029+341',
          value: 'acv',
        },
        {
          label: '交流电流',
          value: 'acc',
        },
        {
          label: '直流电流',
          value: 'dc',
        },
        {
          label: '直流电流密度',
          value: 'dcd',
        },
        {
          label: '交流电流密度',
          value: 'accd',
        },
      ],
      form: {
        region: "cp",
        date1: "",
        date2: ""
      },
      xData,
      yData, //图表数据
      title: '通电电位'
    };
  },
  components: {
    "line-chart": LineChart
  },
  methods: {
    handleTableName(item) {      
      let data = this.dataType.filter(val => item === val.value);
      this.title = data[0].label;      
    }
  },
  mounted() {
    this.$axios.get('api/manager').then(response => {
      console.log(response)
      const res = response.data || {};
      this.xData = res.xData || [];
      this.yData = [
        {
            "name":"管线查询",
            "type":"line",
            "smooth": true,
            "yAxisIndex": 0,
            "data": res.yData || []
        }
      ];
    });
  }
};
</script>
<style>
.toolbar {
  text-align: left;
}
.line {
    text-align: center;
}
.toolbar /deep/ .el-form--inline .el-form-item {
  margin-right: 100px;
}
</style>