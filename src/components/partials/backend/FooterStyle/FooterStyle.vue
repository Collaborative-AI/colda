<template>
   <footer class="iq-footer">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-6">
                <ul class="list-inline mb-0">
                    <li class="list-inline-item"><router-link :to="{name: 'app.privacypolicy'}">Privacy Policy</router-link></li>
                    <li class="list-inline-item"><router-link :to="{name: 'app.Termsofuse'}">Terms of Use</router-link></li>
                </ul>
            </div>
            <div class="col-lg-6 text-right">
                Copyright 2020 <a href="#">{{ appName }}</a> All Rights Reserved.
            </div>
        </div>
    </div>
</footer>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
    name:"Footer",
    prop:{
    },
    computed : {
        ...mapGetters({
            appName: 'appName'
        })
    }
}
</script>