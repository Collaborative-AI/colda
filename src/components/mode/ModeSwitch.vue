<template>
<div class="change-mode">
    <div class="custom-control custom-switch custom-switch-icon custom-control-inline">
        <div class="custom-switch-inner">
            <p class="mb-0"> </p>
            <input type="checkbox" v-model="dark" class="custom-control-input" id="dark-mode" data-active="true">
            <label class="custom-control-label" for="dark-mode" data-mode="toggle">
                <span class="switch-icon-left"><i class="a-left ri-moon-clear-line"></i></span>
                <span class="switch-icon-right"><i class="a-right ri-sun-line"></i></span>
            </label>
        </div>
    </div>
</div>
</template>
<script>
export default {
    name:'ModeSwitch',
    data(){
        return{
            dark:false
        }
    },
    watch:{
     dark:function(){
        this.changeMode()
     }
    },
    methods: {
        changeMode(){
            const body = document.querySelector('body')
            if (this.dark) {
                body.classList.add('dark')
            } else {
                body.classList.remove('dark')
            }
        }
    }
}
</script>