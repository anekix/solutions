<template>
  <div class="home">
  <div class="container">
    <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6">
        <form class="a">
          <fieldset>
            <legend>Form Builder</legend>
            <div class="row">
              <div class="column-sm-4">
                <div class="input-group fluid">
                  <label for="username">Risk</label>
                    <select v-model="selectedRisk" @change="setFields">
                      <option v-for="(value,key) in riskData">{{key}}</option>
                    </select>

                </div>
              </div>
              <div class="column-sm-10">
                <div class="input-group fluid">
                  <label for="pwd">Fields For Risk</label>     
                    <select v-model="selectedField" @change="pushDefaultField(selectedField)">
                      <option v-for="item in fieldsForRisk">{{item}}</option>
                    </select>
                </div>
              </div>
            </div>
          </fieldset>
        </form>  
      </div>
    </div>
  </div>

  <div class="container">
      <div class="row">
          <div class="col-sm-3"></div>
            <div class="col-sm-6">
              <formSegment class ="form-segment" v-for="(row,index) in rows" :rs.sync="row"/>
            </div>
          <div class="col-sm-3"></div>
    </div>
  </div>

        <!--<HelloWorld class ="form-segment" v-for="(row,index) in rows" :rs.sync="row"/>-->
        <!--<button @click="" v-for="(row,index) in rows">Delete</button>-->
      <input type="button" class="button button-outline" value="Add Field" @click="fun">
      <input type="button" class="button button-outline" value="Save Form">
</div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import formSegment from '@/components/formSegment.vue'; // @ is an alias to /src
import axios from 'axios';
import $ from 'jquery' 

@Component({
  components: {
    formSegment,
  },
})

export default class Home extends Vue {
    public rows: {title:string, type:string}[] = [];
    riskData: any = {} ;
    selectedRisk: string="io";
    selectedField: string="";
    fieldsForRisk: String[] = [];
    public tmpr:any = {};
    public fun(): void {
      this.rows.push({title:"",type:""});
  }

    public pushDefaultField(selectedField:string): void {
      this.rows.push({
        title:selectedField,
        type:this.riskData[this.selectedRisk]['fields'][selectedField]['field_type']
        }
      );

  }
    public setFields(): void {
      this.fieldsForRisk = Object.keys(this.riskData[this.selectedRisk].fields);
  }

public mounted(): void {
      this.fetchRisks();
}

public fetchRisks(): void {

  axios.get("api/v1/risk-all")
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
body{
  background-color:white;
}
.a{
  background-color:#F8F8F8;
}
</style>
