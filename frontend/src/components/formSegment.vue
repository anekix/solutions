<template>
  <form class="field-segment">
  <fieldset>
    <legend>Form Builder</legend>
    <div class="row">
      <div class="col-sm-6">
        <div class="input-group fluid">
          <label for="username">Field</label>
          <input type="text" placeholder="Type Field Name" v-model="rs.title"/>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="input-group fluid">
          <label for="pwd">Type</label>     
            <select v-model="rs.type">
              <option>NUMBER</option>
              <option>TEXT</option>
              <option>DATE</option>
            </select>
        </div>
      </div>
    </div>

    <div class="row" v-if="rs.type=='TEXT'">
      <div class="col-sm-6">
        <div class="input-group fluid">
          <label for="input">Input</label>
          <input type="text"></input>
        </div>
      </div>
    </div>

    <div class="row" v-if="rs.type=='DATE'">
      <div class="col-sm-6">
        <div class="input-group fluid">
          <label for="input">Input</label>
          <input type="Date"></input>
        </div>
      </div>
    </div>
    <div class="row" v-if="rs.type=='NUMBER'">
      <div class="col-sm-6">
        <div class="input-group fluid">
          <label for="input">Input</label>
          <input type="number"></input>
        </div>
      </div>
    </div>
  </fieldset>
</form>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class formSegment extends Vue {
  @Prop() private msg!: string;
  
  @Prop({default: {}}) 
  private rs: any;
  private widgetTypeSeleted:string='';
  // @Prop() public ds: { label: string, value: string }[] = [];
  // public lds: { label: string, value: string }[] = [];
  // public asyncOK(): void {
  //    this.$emit("update:ds", this.ds);
 
  // }
  // // this.$emit('update:ds', ds);

  // public ds:{questiom:string, answer:string}[] = [{
  //   question:"",answer:""
  // }];

}
</script>
<style>
.field-segment:hover{
  border-left:4px solid blue;
}
</style>
