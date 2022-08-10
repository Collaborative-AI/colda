<template>
  <li :class="liClass">
    <a :class="'nav-link '+className+' '+widthclass" :id="id" :data-toggle="dataToggle" :href="url" :role="role" :aria-controls="ariaControls" :aria-selected="ariaSelected">
      <slot name="title" v-if="hasTitleSlot"/>
      <template v-else>{{ title }}</template>
    </a>
  </li>
</template>
<script>
export default {
  name: 'tab-nav-items',
  props: {
    id: { type: String, default: 'myTab' },
    active: { type: Boolean, default: false },
    role: { type: String, default: 'tab' },
    ariaControls: { type: String, default: 'tabpanel' },
    ariaSelected: { type: Boolean, default: false },
    dataToggle: { type: String, default: 'tab' },
    href: { type: String, default: '' },
    title: { type: String, default: '' },
    liClass: { type: String, default: 'nav-item' },
    widthclass: { type: String, default: null }
  },
  mounted () {
    if (this.active) {
      this.className = 'show active'
    }
  },
  computed: {
    hasTitleSlot () {
      return !!this.$slots.title
    },
    url () {
      if (this.href === '') {
        return '#' + this.ariaControls
      }
      return this.href
    }
  },
  data () {
    return {
      className: ''
    }
  }
}
</script>
