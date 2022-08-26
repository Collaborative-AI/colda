<template>
  <b-collapse tag="ul" :class="className" :visible="open" :id="idName" :accordion="accordianName">
    <li v-for="(item,index) in items" :key="index"
        :class="activeLink(item) && item.children ? 'active' : activeLink(item) ? 'active' : ''">
      <router-link :to="item.link" v-if="!item.is_heading" :class="`iq-waves-effect ${activeLink(item) && item.children ? 'active' : activeLink(item) ? 'active' : ''}`" v-b-toggle="item.name" >
        <i v-if="item.name && hideListMenuTitle" :class="item.icon_class ? item.icon_class  :''"></i>
        <template v-else v-html="item.icon">
        </template>
        <span>{{ item.title }}</span>
        <i v-if="item.children && $route.name !='backend.layout-4'" :class="item.expanded_icon_class" />
        <i v-if="item.children && $route.name !='backend.layout-4'" :class="item.collapse_icon_class" />
        <small v-html="item.append" v-if="hideListMenuTitle" :class="item.append_class" />
      </router-link>
      <List v-if="item.children" :items="item.children" :sidebarGroupTitle="hideListMenuTitle"
            :open="activeLink(item) && item.children ? true : activeLink(item) ? true : false"
            :idName="item.name" :accordianName="`sidebar-accordion-${item.class_name}`" :className="`iq-submenu ${item.class_name}`" />
    </li>
  </b-collapse>
</template>
<script>
import List from './CollapseMenu'
import { core } from '@/config/pluginInit'
export default {
  name: 'List',
  props: {
    items: Array,
    className: { type: String, default: 'iq-menu' },
    open: { type: Boolean, default: false },
    idName: { type: String, default: 'sidebar' },
    accordianName: { type: String, default: 'sidebar' },
      sidebarGroupTitle: { type: Boolean, default: true }
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
