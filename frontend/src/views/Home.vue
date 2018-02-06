<template>
  <div class="home">
    <div id="risk-selector container">
      <div class="row">


        <div class="column">
          <select v-model="selectedRisk" @change="setFields">
          <option v-for="(value,key) in riskData">{{key}}</option>
          </select>
        </div>
        <div class="column">
          <select v-model="selectedField" @change="fun(field,type)">
          <option v-for="item in fieldsForRisk">{{item.field_name}}</option>
          </select>
        </div>
      </div>
    </div>

  <div class="row">
    <div class="column">
      <span id="header"> ADD FIELDS FOR CUSTOM RISK</span>
    </div>
  </div>

    <HelloWorld v-for="(row,index) in rows" :rs="row"/>
    <input type="button" class="button button-outline" value="Add Field" @click="fun">
    <input type="button" class="button button-outline" value="Save Form" @click="fun">

  </div>
  
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
import axios from 'axios';
import $ from 'jquery' 

@Component({
  components: {
    HelloWorld,
  },
})
// function addComp(){
//   alert("hi");
// // const vueContainer = document.createElement('div')
// // // add it to `div#app`
// // container.appendChild(vueContainer)
// // // mount the Vue component to the ephemeral div, which Vue will remove from DOM
// // vm = ( new ( Vue.extend(App) ) ).$mount(vueContainer)
// }


export default class Home extends Vue {
    public rows: {title:''}[] = [];
    riskData: any = {} ;
    selectedRisk: string="io";
    fieldsForRisk: String[] = [];
    // public selectedSegment: number = 0;
    // public data_structure:  { label: string, value: string }[] = [{
    //     label:'',
    //     value:'',
    //   }];
    public fun(): void {
      this.rows.push({title:""});
  }

    public setFields(): void {
      // alert(JSON.stringify(this.riskData));
      // alert(this.)
      this.fieldsForRisk = this.riskData[this.selectedRisk].fields;

  }

public mounted(): void {

      this.fetchRisks();
      


}

  public fetchRisks(): void {

  axios.get("api/risk-all")
    .then((response) => {
      console.log(response);
      this.riskData = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
    }


}

</script>

<style>
#risk-selector{
  width:50%;

}

table{
  width:50%;
  justify:center;
}
#header{
  color:#9B4CDA;
  font-size:13px;
}
</style>
