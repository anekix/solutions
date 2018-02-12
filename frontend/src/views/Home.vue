<template>
  <div class="home">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3" id="sidebar">
            <div class="risk" v-for="(item,index) in riskData" @click="setTemplate(index)">
            {{item.risk}} 
            <!--<span class="risk-id"> {{item.risk_id}}</span>-->
            </div>
        </div>
        <div class="col-sm-9 content" id="style-1">
          <div class="row nav">
            <div class="col-sm-4">
              <div class="button-group">
                <button class="mode-buttons" @click="cleanCanvas">New Form</button>
                <button class="mode-buttons" @click="toggleFormPreview">{{mode}}</button>
                <button class="mode-buttons">Save</button>
              </div>
            </div>
            <div class="col-sm-8">
              <i class="material-icons md-48" id="user-icon">account_circle</i>
            </div>
          </div>
        <div class="row">
          <div class="col-sm-3"></div>
            <span class="info" v-if="rows.length==0">Try selecting a template on left or Create a new form!</span>
        </div>
        <div class="row animated bounceIn" v-if="mode=='edit'">
              <div class="col-sm-2">
              </div>
              <div class="col-sm-8">
                <form class="preview">
                    <div class="row" v-for="row in rows">
                      <div class="col-sm-5">
                        <div class="input-group fluid">
                          <label for="username">{{row.title}}</label>
                        </div>
                      </div>

                      <div class="col-sm-5">
                        <div class="input-group fluid">
                            <div class="input-group fluid" v-if="row.type=='TEXT'">
                          <input type="text"></input>
                        </div>

                        <div class="input-group fluid" v-if="row.type=='DATE'">
                          <input type="Date"></input>
                        </div>


                        <div class="input-group fluid" v-if="row.type=='NUMBER'">
                          <input type="number"></input>
                        </div>
                        </div>
                      </div>
                    </div>
                </form>
          </div>
        </div>

        <div class="row" v-for="(row,index) in rows"  v-if="mode=='preview'">
          <div class="col-sm-2">
          </div>
          <div class="col-sm-8">
            <formSegment class ="form-segment" :rs.sync="row"/>
          </div>
          <div class="col-sm-2">
            <span class="close close-btn" @click="removeSegment(index)"></span>
          </div>
        </div>
         <div class="row">
          <div class="col-sm-5">
          </div>
         <button class="tertiary large" @click="fun">Add field</button>
         </div>
      </div>
        </div>
        </div>
      </div>
    </div>
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
    public mode: string = 'preview';
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


    public removeSegment(index:number): void {
      this.rows.splice(index, 1);
  }

    public toggleFormPreview():void{
      if (this.mode == 'preview'){
        this.mode = 'edit'
      }
      else{
        if (this.mode == 'edit'){
        this.mode = 'preview'
      }  
      }
    }

    public cleanCanvas(): void {
      this.rows = [];
  }

    public setFields(): void {
      this.fieldsForRisk = Object.keys(this.riskData[this.selectedRisk].fields);
  }
    public setTemplate(index:number): void {
        var self = this;
        this.rows = [];
        Object.keys(self.riskData[index].fields).forEach(function(key) {
            console.log(self.riskData[index].fields[key].field_type);
            self.rows.push({title:key , type:self.riskData[index].fields[key].field_type})
            // this.$store.commit('setRisks',{title:key , type:self.riskData[index].fields[key].field_type}) // set the user in the store

        });


  }

    public mounted(): void {
      this.fetchRisks();

  }


    public fetchRisks(): void {

      axios.get("api/v1/risk-all")
        .then((response) => {
          console.log(response);
          this.riskData = response.data.data;
          console.log(this.riskData);
          this.$store.commit('setRisks', response.data.data) // set the user in the store
          console.log(this.$store.state.risks) // access the user
    })
    .catch((error) => {
      console.log(error);
    });
  }


}

</script>

<style>
.mode-buttons{
font-family: 'Bree Serif', serif;
}
.info{
background-color:lightblue;
border-radius:8px;
padding-left:8px;
padding-right:8px;
color:black;

}

.preview{
  background-color:white;
  border-left:2px solid blue;
  
}
.close-btn{
  margin-top:10px;
}

.risk-id{
  float:right;
  padding-right:10px;
  padding-left:10px;
  border-radius:10px;
  background-color:lightblue;
  color:white;
}
#user-icon:{
    float:right;
    color:white;
}
.material-icons.md-48 { font-size: 48px; color:#f19066;float:right; display:block;}

.nav{
  background-color:#fafafa;
  
}
.temp{
  background-color:red;
}
.content{
  // background-color:green;
  overflow: auto;
max-height: 100vh;

}
.header{
  // background-color:red;
}
#sidebar{
  height:100vh;
  background-color:#ffffff;

}

.risk{
  padding-top:10px;
  padding-bottom:10px; 
  padding-left:20px; 
  font-family: 'Bree Serif', serif;

}

.risk:hover{
  background-color:#f2f2f2;
  cursor:pointer;
}
#risk-selector{
  width:50%;

}
.risk-selector{
  height:100vh;
  width:20%;
}
body{
  background-color:#E6E6E6;
  padding:0px;
margin:0px;

}
.a{
  background-color:#F8F8F8;
}

.remove-segment-button:hover{
background-color:red;
}
.close{
  background-color:lightblue;
  color:white;
}
.close:hover{
  background-color:blue;
}
.risk-selector{
  background-color:#f1f1f1;
    color:black;
    border-right:1px solid blue;
    //box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0.75);


  padding-top:8px;
  padding-bottom:8px;
    list-style-type: none;


}
.risk-selector:hover{
  background-color:darkgrey;
}




#hover {
    background: #eeeeee;
    padding: 6px;
    display: block;
    position: relative;
}

#hover:hover {
    background: #dddddd;
    
}



#popup {
    opacity: 0;
    position: absolute;
    top: 32px;
    background: #fafafa;
    border: 1px solid transparent;
    border-radius: 6px;
    height: 0px;
    padding: 0 12px;
    overflow: hidden;
    -webkit-transition: all 500ms;
    transition: all 500ms;
}


#hover:hover #popup {
    padding: 12px 12px;
    height: auto;
    opacity: 1;
    border: 1px solid #eeeeee;
}


#style-1::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	border-radius: 10px;
	background-color: #F5F5F5;
}

#style-1::-webkit-scrollbar
{
	width: 12px;
	background-color: #F5F5F5;
}

#style-1::-webkit-scrollbar-thumb
{
	border-radius: 10px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color: #555;
}

</style>
