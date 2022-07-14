<template>
  <div class="sidebar">
    <div class="menu">
      <ul>
        <li :class="active === 1 && 'active'">
          <router-link
            :class="active === 1 && 'active'"
            :to="darkLink('dashboard')"
            data-toggle="tooltip"
            data-placement="right"
            title="Trade"
          >
            <span><i class="mdi mdi-view-dashboard"></i></span>
          </router-link>
        </li>
        <li :class="active === 2 && 'active'">
          <router-link
            :class="active === 2 && 'active'"
            :to="darkLink('exchange')"
            data-toggle="tooltip"
            data-placement="right"
            title="Exchange"
          >
            <span><i class="mdi mdi-tumblr-reblog"></i></span>
          </router-link>
        </li>
        <li :class="active === 3 && 'active'">
          <router-link
            :class="active === 3 && 'active'"
            :to="darkLink('account-overview')"
            data-toggle="tooltip"
            data-placement="right"
            title="Accounts"
          >
            <span><i class="mdi mdi-face-profile"></i></span>
          </router-link>
        </li>
        <li :class="active === 4 && 'active'">
          <router-link
            :class="active === 4 && 'active'"
            :to="darkLink('data-tbi')"
            data-toggle="tooltip"
            data-placement="right"
            title="Data"
          >
            <span><i class="mdi mdi-database"></i></span>
          </router-link>
        </li>
        <li :class="active === 5 && 'active'">
          <router-link
            :class="active === 5 && 'active'"
            :to="darkLink('settings')"
            data-toggle="tooltip"
            data-placement="right"
            title="Setting"
          >
            <span><i class="mdi mdi-settings"></i></span>
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
  props: {
    active: Number,
    dark: Boolean,
  },
  methods: {
    darkLink(name) {
      if (this.dark) {
        return `/${name}-dark`;
      } else {
        return `/${name}`;
      }
    },
  },
};
</script>
