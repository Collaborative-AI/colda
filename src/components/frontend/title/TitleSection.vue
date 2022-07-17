<template>
  <div :class="'row'+' '+ mainclass">
    <div :class="'col-lg-6 col-md-6 wow fadeIn'+' '+ topclass">
      <div :class="'text-left iq-title-box'+' '+subclass">
        <h2 :class="'iq-title text-uppercase' +' '+ titleclass">
          {{ title }}
        </h2>
        <slot name="underline" />
      </div>
    </div>
    <slot name="rightside" />
  </div>
</template>
<script>
export default {
  name: 'TitleSection',
  props: {
    title: {
      type: String,
      default: ''
    },
    subclass: {
      type: String,
      default: ''
    },
    titleclass: {
      type: String,
      default: ''
    },
    mainclass: {
      type: String,
      default: ''
    },
    topclass: {
      type: String,
      default: ''
    }
  }
}
</script>
