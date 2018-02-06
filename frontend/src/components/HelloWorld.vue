<template>
  <div class="segment">
      <div class="container">
        <div class="row">
          <div class="column">
            <input type="text" placeholder="Type Field Name" v-model="rs.title"/>
          </div>
          <div class="column">
  <select>
    <option>{{rs.type}}</option>
    <option>Checkbox</option>
    <option>TextBox</option>
  </select>
          </div>
      </div>
      </div>
</div>

</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class HelloWorld extends Vue {
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

</style>
