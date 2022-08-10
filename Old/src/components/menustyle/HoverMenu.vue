<template>
  <ul tag="ul" :class="className" :id="idName">
    <li v-for="(item,index) in items" :key="index" :class="item.is_heading ? 'iq-menu-title' :''">
      <i v-if="item.is_heading && hideListMenuTitle" class="ri-subtract-line" />
      <span v-if="item.is_heading">{{ $t(item.name) }}</span>
      <router-link :to="item.link" v-if="!item.is_heading" :class="`iq-waves-effect`">
        <i v-if="item.name && hideListMenuTitle" :class="item.icon_class ? item.icon_class  :''"></i>
        <template v-else v-html="item.icon">
        </template>
        <span>{{ item.title }}</span>
        <template v-if="item.children && enableIcon">
          <template v-if="enableCustomIcon"> 
            <i :class="item.expanded_icon_class"></i>
            <i :class="item.collapse_icon_class"></i>
          </template>
          <i v-else class="ri-arrow-right-s-line iq-arrow-right" />
        </template>
        <small v-html="item.append" v-if="hideListMenuTitle" :class="item.append_class" />
      </router-link>
      <List v-if="item.children" :items="item.children" :sidebarGroupTitle="hideListMenuTitle" :idName="item.name" :className="`iq-submenu ${item.class_name}`" />
    </li>
  </ul>
</template>
<script>
import List from './CollapseMenu'
import { core } from '@/config/pluginInit'
export default {
  name: 'List',
  props: {
    items: Array,
    className: { type: String, default: 'iq-menu d-flex' },
    open: { type: Boolean, default: false },
    idName: { type: String, default: 'iq-sidebar-toggle' },
    sidebarGroupTitle: { type: Boolean, default: true },
    enableCustomIcon:  {type: Boolean, default: false},
    enableIcon: {type: Boolean, default: true}
  },
  components: {
    List
  },
  computed: {
    hideListMenuTitle () {
      return this.sidebarGroupTitle
    }
  },
  mounted () {
  },
  methods: {
    activeLink (item) {
      return core.getActiveLink(item, this.$route.name)
    }
  }
}
</script>

<style scoped>
  .iq-submenu{
    max-height: 300px;
    overflow-y: scroll;
  }
</style>
