<template>
  <form class="field-segment">
    <div class="row">
      <div class="col-sm-6">
        <div class="input-group fluid">
          <label for="username">Field</label>
          <input type="text" placeholder="Type Field Name" v-model="rs.title"/>
        </div>
      </div>
      <div class="col-sm-5">
        <div class="input-group fluid">
          <label for="pwd">Type</label>     
            <select v-model="rs.type">
              <option>NUMBER</option>
              <option>TEXT</option>
              <option>DATE</option>
            </select>
        </div>
      </div>
      <div class="col-sm-1">
              <div class="input-group fluid">

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
}
</script>
<style>
.field-segment{
  background-color: white;
}

.field-segment:hover{
  border-left:4px solid blue;
}
.close{
  // padding-top:0px !important;
  // margin-top:0px;
}

/* Safari 4.0 - 8.0 */
@-webkit-keyframes example {
    from {background-color: red;}
    to {background-color: yellow;}
}

/* Standard syntax */
@keyframes example {
    from {border-left: 4px solid blue;}
    to {border-left: 4px solid yellow;}
}
.head{
  background-color:blue;
}
</style>
