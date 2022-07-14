import Vue from "vue";
import VueRouter from "vue-router";
// Link
import Demo from "./views/Demo";
// Landing
import Landing from "./views/Landing"
// auth
import Signin from "./views/auth/Signin";
import Signup from "./views/auth/Signup";
import Lock from "./views/auth/Lock";
import Otp1 from "./views/auth/Otp1";
import Otp2 from "./views/auth/Otp2";
import Reset from "./views/auth/Reset";
// Dashboard
import Dashboard from "./views/Dashboard/Dashboard.vue"
// import HomeDark from "./views/Dashboard/HomeDark"
import Exchange from "./views/Dashboard/Exchange"
// Account
import Overview from "./views/Dashboard/Account/Overview"
import API from "./views/Dashboard/Account/API"
import Affiliate from "./views/Dashboard/Account/Affiliate"
import Deposit from "./views/Dashboard/Account/Deposit"
import Withdraw from "./views/Dashboard/Account/Withdraw"
// Data
import Tbi from "./views/Dashboard/Data/Tbi"
import Founding from "./views/Dashboard/Data/Founding"
import IndexPrice from "./views/Dashboard/Data/IndexPrice"
import Insurance from "./views/Dashboard/Data/Insurance"
import LastPrice from "./views/Dashboard/Data/LastPrice"
import MarkPrice from "./views/Dashboard/Data/MarkPrice"
// Setting
import EditProfile from "./views/Dashboard/Settings/EditProfile"
import Account from "./views/Dashboard/Settings/Account"
import Preferences from "./views/Dashboard/Settings/Preferences"
import Security from "./views/Dashboard/Settings/Security"
// verify step
import VerifyStep1 from "./views/Dashboard/VerifyStep1"
import VerifyStep2 from "./views/Dashboard/VerifyStep2"
import VerifyStep3 from "./views/Dashboard/VerifyStep3"
import VerifyStep4 from "./views/Dashboard/VerifyStep4"
import VerifyStep5 from "./views/Dashboard/VerifyStep5"
import VerifyStep6 from "./views/Dashboard/VerifyStep6"
// Card add
import AddBankAcc from "./views/Dashboard/AddBankAcc"
import AddDebitCard from "./views/Dashboard/AddDebitCard"
// Errors
import E400 from "./views/errors/400"
import E403 from "./views/errors/403"
import E404 from "./views/errors/404"
import E500 from "./views/errors/500"
import E503 from "./views/errors/503"

//import our website
import Products from './views/Products.vue'
import Usecases from './views/Usecases.vue'
import About from './views/About.vue'
import Contact from './views/Contact.vue'
import Modules from './views/LandingCopy.vue'



Vue.use(VueRouter);

const routes = [
  // our website page
  { path: "/products", name: "Products", component: Products},
  { path: "/products", name: "Products", component: Products},
  { path: "/about", name: "About", component: About},
  { path: "/contact", name: "Contact", component: Contact},
  { path: "/usecases", name: "Usecases", component: Usecases},
  { path: "/modules", name: "Modules", component: Modules},
  // Dashboard
  { path: "/dashboard", name: "Dashboard", component: Dashboard },
  { path: "/exchange", name: "Exchange", component: Exchange },
  // Errors
  { path: "/400", name: "E400", component: E400 },
  { path: "/403", name: "E403", component: E403 },
  { path: "/404", name: "E404", component: E404 },
  { path: "/500", name: "E500", component: E500 },
  { path: "/503", name: "E503", component: E503 },
  // Add card
  { path: "/add-bank-acc", name: "AddBankAcc", component: AddBankAcc },
  { path: "/add-debit-card", name: "AddDebitCard", component: AddDebitCard },
  // verify step
  { path: "/verify-step-1", name: "VerifyStep1", component: VerifyStep1 },
  { path: "/verify-step-2", name: "VerifyStep2", component: VerifyStep2 },
  { path: "/verify-step-3", name: "VerifyStep3", component: VerifyStep3 },
  { path: "/verify-step-4", name: "VerifyStep4", component: VerifyStep4 },
  { path: "/verify-step-5", name: "VerifyStep5", component: VerifyStep5 },
  { path: "/verify-step-6", name: "VerifyStep6", component: VerifyStep6 },
  // Setting
  { path: "/settings", name: "EditProfile", component: EditProfile },
  { path: "/settings-account", name: "Account", component: Account},
  { path: "/settings-preferences", name: "Preferences", component: Preferences },
  { path: "/settings-security", name: "Security", component: Security },
  // Data
  { path: "/data-tbi", name: "Tbi", component: Tbi },
  { path: "/data-mark-price", name: "MarkPrice", component: MarkPrice },
  { path: "/data-founding-rate", name: "Founding", component: Founding },
  { path: "/data-index-price", name: "IndexPrice", component: IndexPrice },
  { path: "/data-insurance-found", name: "Insurance", component: Insurance },
  { path: "/data-last-price", name: "LastPrice", component: LastPrice },
  // Dashboard overly
  { path: "/account-withdraw", name: "Withdraw", component: Withdraw },
  { path: "/account-deposit", name: "Deposit", component: Deposit },
  { path: "/account-affiliate", name: "Affiliate", component: Affiliate },
  { path: "/account-api", name: "API", component: API },
  { path: "/account-overview", name: "Overview", component: Overview },
  // demo
  { path: "/demo", name: "Demo", component: Demo },
  { path: "/", name: "Landing", component: Landing },
  // Auth
  { path: "/signin", name: "Signin", component: Signin },
  { path: "/signup", name: "Signup", component: Signup },
  { path: "/reset", name: "Reset", component: Reset },
  { path: "/lock", name: "Lock", component: Lock },
  { path: "/otp-1", name: "Otp1", component: Otp1 },
  { path: "/otp-2", name: "Otp2", component: Otp2 },

// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Dark <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

  // Dashboard
  { path: "/dashboard-dark", name: "HomeDark", component: Dashboard },
  { path: "/exchange-dark", name: "Exchange", component: Exchange },
  // Errors
  { path: "/400-dark", name: "E400", component: E400 },
  { path: "/403-dark", name: "E403", component: E403 },
  { path: "/404-dark", name: "E404", component: E404 },
  { path: "/500-dark", name: "E500", component: E500 },
  { path: "/503-dark", name: "E503", component: E503 },
  // Add card
  { path: "/add-bank-acc-dark", name: "AddBankAcc", component: AddBankAcc },
  { path: "/add-debit-card-dark", name: "AddDebitCard", component: AddDebitCard },
  // verify step
  { path: "/verify-step-1-dark", name: "VerifyStep1", component: VerifyStep1 },
  { path: "/verify-step-2-dark", name: "VerifyStep2", component: VerifyStep2 },
  { path: "/verify-step-3-dark", name: "VerifyStep3", component: VerifyStep3 },
  { path: "/verify-step-4-dark", name: "VerifyStep4", component: VerifyStep4 },
  { path: "/verify-step-5-dark", name: "VerifyStep5", component: VerifyStep5 },
  { path: "/verify-step-6-dark", name: "VerifyStep6", component: VerifyStep6 },
  // Setting
  { path: "/settings-dark", name: "EditProfile", component: EditProfile },
  { path: "/settings-account-dark", name: "Account", component: Account},
  { path: "/settings-preferences-dark", name: "Preferences", component: Preferences },
  { path: "/settings-security-dark", name: "Security", component: Security },
  // Data
  { path: "/data-tbi-dark", name: "Tbi", component: Tbi },
  { path: "/data-mark-price-dark", name: "MarkPrice", component: MarkPrice },
  { path: "/data-founding-rate-dark", name: "Founding", component: Founding },
  { path: "/data-index-price-dark", name: "IndexPrice", component: IndexPrice },
  { path: "/data-insurance-found-dark", name: "Insurance", component: Insurance },
  { path: "/data-last-price-dark", name: "LastPrice", component: LastPrice },
  // Dashboard overly
  { path: "/account-withdraw-dark", name: "Withdraw", component: Withdraw },
  { path: "/account-deposit-dark", name: "Deposit", component: Deposit },
  { path: "/account-affiliate-dark", name: "Affiliate", component: Affiliate },
  { path: "/account-api-dark", name: "API", component: API },
  { path: "/account-overview-dark", name: "Overview", component: Overview },
  // demo
  { path: "/demo-dark", name: "Demo", component: Demo },
  { path: "/dark", name: "Landing", component: Landing },
  // Auth
  { path: "/signin-dark", name: "Signin", component: Signin },
  { path: "/signup-dark", name: "Signup", component: Signup },
  { path: "/reset-dark", name: "Reset", component: Reset },
  { path: "/lock-dark", name: "Lock", component: Lock },
  { path: "/otp-1-dark", name: "Otp1", component: Otp1 },
  { path: "/otp-2-dark", name: "Otp2", component: Otp2 },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
