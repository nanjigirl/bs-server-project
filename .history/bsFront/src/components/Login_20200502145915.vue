<template>
    <div class="login">
        <div class="login-box">
            <img class="login-logo" src="../assets/images/zsylogo.png" alt />
            <p class="logo-name">管道阴极保护智能分析系统</p>
            <el-form :model="userForm" status-icon ref="userForm" label-width="100px" class="user-form">
                <el-form-item prop="username">
                    <el-input type="text" prefix-icon="el-icon-search" placeholder="账号" v-model="userForm.username" autoComplete="off">
                        <template slot="prepend"><i class="icon iconfont icon-gerenzhongxinyonghu01"></i></template>
                    </el-input>                
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="密码" v-model="userForm.password" autoComplete="off">
                        <template slot="prepend"><i class="icon iconfont icon-mima"></i></template>
                    </el-input>
                </el-form-item>
                <div class="pws-box">
                    <el-checkbox class="remenber" v-model="checked">记住密码</el-checkbox> 
                    <el-button class="forget" type="text">忘记密码？</el-button>  </div>       
                <el-form-item>
                    <el-button @click="submitForm">登录</el-button>                
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>    
    export default {
        data () {
            return {
                checked: false,
                userForm:{
                    username: '',
                    password: ''
                }
            }
        },
        methods: {
            submitForm() {
                console.log('login',this.userForm)
                if (this.userForm.username === 'abc' && this.userForm.password === 'abc')
                    this.$router.push('/DataManager');
                else this.$message.error('账号或密码错误！');
            }
        },
        mounted() {
          axios.get('api/login').then(response => {

          });
        }    
    }
</script>
<style>
    .login {
        width: 100%;
        height: 100%;
        background: #324157;
    }
    .login-box {
        text-align: center;
        position: absolute;
        top: 45%;
        left: 50%;        
        transform: translate(-50%, -50%);
    }
    .login-logo {
        width: 180px;
        height: 180px;        
    }    
    .logo-name {
        color: #fff;
        font-size: 20px;
        margin: 5px 0 18px;
    }
    .user-form .el-form-item__content {
        margin: 0!important;
    }
    .user-form .el-input__inner {
        background: rgba(0,0,0,.2);
        color: #fff;
    }
    .user-form .el-input-group__prepend {
        background: rgba(0,0,0,.2);
        color: #fff;
    }
    .user-form .el-button {
        background: rgba(0,0,0,.2);
        color: #fff;
    }
    .user-form .pws-box {        
        position: relative;
        top: -20px;            
        color: #999;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .user-form .forget {
        background: none;
        color: #999;
    }
    .user-form .remenber {        
        color: #999;
    }
</style>
