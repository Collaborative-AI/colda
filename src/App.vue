<template>
    <div>   
        <router-view />
        <!-- <Preloader v-if="isLoading" /> -->
        <GoTop /> 
    </div>
</template>

<script>
    // import Preloader from './components/Layout/Preloader'
    import GoTop from './components/Layout/GoTop'
    export default {
        name: 'App',
        components: {
            // Preloader,
            GoTop,
        },
        data() {
            return {
                isLoading: true,
                activeItem: 1
            }
        },
        mounted() {
            setTimeout(() => {
                this.isLoading = false
            }, 2000)
        },
//         beforeMount() {
//     this.activeItem = this.$route.matched[0].props.default.page;
//   },
  
    }
</script>

<style scoped>

</style>
