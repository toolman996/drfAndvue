<template>
    <div id="wrap">
			<div id="top_content">
				<div id="header">
					<div id="rightheader">
						<p>
							2020/7/7
							<br />
                            <a href="javascript:;" style="text-decoration: none" @click="quit">安全退出</a>
						</p>
					</div>
					<div id="topheader">
						<h1 id="title">
							<a href="#">main</a>
						</h1>
					</div>
					<div id="navigation">
					</div>
				</div>
				<div id="content">
					<p id="whereami">
					</p>
					<h1>
						Welcome:{{user}}
					</h1>
					<table class="table">
						<tr class="table_header">
							<td>
								ID
							</td>
							<td>
								Name
							</td>
							<td>
								Photo
							</td>
							<td>
								Salary
							</td>
							<td>
								Age
							</td>
							<td>
								Operation
							</td>
						</tr>
						<tr class="row1" v-for="(emp,index) in list" :key="emp.id" :class="index%2==0?'row1':'row2'">
							<td>
								{{emp.id}}
							</td>
							<td>
								{{emp.emp_name}}
							</td>
							<td>
								<img :src="emp.img" style="height: 60px;">
							</td>
<!--                            <td>-->
<!--								{{emp.img}}-->
<!--							</td>-->
							<td>
								{{emp.salary}}
							</td>
							<td>
								{{emp.age}}
							</td>
							<td>
								<a href="javascript:;" @click="del(emp.id)">delete emp</a>&nbsp;
                                <router-link :to="'/update/'+emp.id">update emp</router-link>
<!--                                <router-link :to="'/update/'+emp.id+'/'+emp.emp_name+'/'+emp.salary+'/'+emp.age">update emp</router-link>-->
							</td>
						</tr>

					</table>
					<p>
						<el-button  plain ><router-link to="/addemp">添加员工</router-link></el-button>
					</p>
				</div>
			</div>
			<div id="footer">
				<div id="footer_bg">
				ABC@126.com
				</div>
			</div>
		</div>
</template>

<script>
    export default {
        name: "Index",
        data(){
            return{
                user:'',
                list:[]
            }
        },
        methods:{
            fun(){
                this.$axios.get('http://127.0.0.1:8000/emsapp/emp/').then(res=>{
                    this.list=res.data.result
                    console.log(this.list)
                }).catch(error => {
                    this.$message.error('查询出错');
                })
            },
            del(id){
                this.$axios({
                url:'http://127.0.0.1:8000/emsapp/emp/'+`${id}`,
                method:'delete',
                // data:{
                //     id:id,
                // },

              }).then(res=>{
                  this.$message('删除成功');
                  location.reload();
              }).catch(error=>{
                  this.$message.error('删除失败');
              })
            },
            quit(){
                sessionStorage.clear();
                this.$router.push('/login')
            }
        },
        created() {
            let bt=sessionStorage.getItem('user')
            this.user=bt
            if (bt){

            }else {
                this.$message.error('请先登录')
                this.$router.push('/login')
            }
            this.fun()
        }
    }
</script>

<style scoped>

</style>
