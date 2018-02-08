<template>
  <form class="field-segment">
  <fieldset>
    <legend>Form Builder</legend>
    <div class="row">
      <div class="column-sm-4">
        <div class="input-group fluid">
          <label for="username">Field</label>
          <input type="text" placeholder="Type Field Name" v-model="rs.title"/>
        </div>
      </div>
      <div class="column-sm-10">
        <div class="input-group fluid">
          <label for="pwd">Type</label>     
            <select>
              <option>{{rs.type}}</option>
              <option>Checkbox</option>
              <option>TextBox</option>
            </select>
        </div>
      </div>
    </div>
  </fieldset>
  

</form>
</div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class formSegment extends Vue {
  @Prop() private msg!: string;
  
  @Prop({default: {}}) 
  private rs: any;
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
