<template>
  <div class="page-title dashboard">
    <div class="container">
      <div class="row">
        <div class="col-6">
          <div class="page-title-content">
            <p>
              Welcome Back,
              <span> Sabuj Hasan Sarker</span>
            </p>
          </div>
        </div>
        <div class="col-6">
          <ul class="text-right breadcrumbs list-unstyle">
            <li>
              <router-link :to="dark ? 'settings-dark' : 'settings'"
                >Settings
              </router-link>
            </li>
            <li class="active"><router-link to="#">Security</router-link></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Title",
  props: {
    dark: Boolean,
  },
};
</script>
