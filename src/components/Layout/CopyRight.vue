<template>
    <div class="copyright-area">
        <div class="container">
            <div class="copyright-area-content">
                <div class="row align-items-center">
                    <div class="col-lg-6 col-md-6">
                        <p>
                            Copyright &copy; {{currentYear}} Synspot. All Rights Reserved
                            <!-- <a href="https://envytheme.com/" target="_blank">
                                EnvyTheme
                            </a> -->
                        </p>
                    </div>

                    <div class="col-lg-6 col-md-6">
                        <ul>
                            <li>
                                <router-link to="/terms-condition">Terms & Conditions</router-link>
                            </li>
                            <li>
                                <router-link to="/privacy-policy">Privacy Policy</router-link>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CopyRight',
    data() {
        return {
            currentYear: new Date().getFullYear(),
        };
    }
}
</script>