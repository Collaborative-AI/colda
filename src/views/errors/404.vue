<template>
  <errors-layouts>
    <h1 class="error-text font-weight-bold">404</h1>
    <h4 class="mt-4">
      <i class="fa fa-exclamation-triangle text-warning"></i> The page you were
      looking for is not found!
    </h4>
    <p>You may have mistyped the address or the page may have moved.</p>
  </errors-layouts>
</template>

<script>
import ErrorsLayouts from "../../components/Layouts/ErrorsLayouts.vue";
export default {
  components: { ErrorsLayouts },
};
</script>
