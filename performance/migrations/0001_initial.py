# Generated by Django 2.2 on 2020-02-16 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstantData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='日期')),
                ('month_plan_order_number', models.IntegerField(verbose_name='当月约定订单数')),
                ('target_cost', models.FloatField(verbose_name='目标成本')),
                ('field_management_compliance_target_number', models.IntegerField(verbose_name='现场管理标准目标数')),
                ('annual_target_turnover', models.FloatField(verbose_name='年度目标营业额')),
                ('annual_target_award', models.FloatField(verbose_name='年度目标奖金额')),
            ],
            options={
                'verbose_name': '常量数据',
                'verbose_name_plural': '常量数据',
                'permissions': (('manage_constant_data', '管理常量数据'),),
            },
        ),
        migrations.CreateModel(
            name='InternalControlIndicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='日期')),
                ('order_number', models.CharField(max_length=100, verbose_name='订单号')),
                ('scheduled_delivery', models.DateTimeField(verbose_name='计划交期')),
                ('actual_delivery', models.DateTimeField(verbose_name='实际交期')),
                ('finished_number', models.IntegerField(verbose_name='完成数')),
                ('unfinished_number', models.IntegerField(verbose_name='未完成数')),
                ('target_well_done_rate', models.FloatField(verbose_name='目标成品率')),
                ('actual_well_done_rate', models.FloatField(verbose_name='实际成品率')),
                ('month_medical_expenses', models.FloatField(verbose_name='当月医药费')),
                ('cost_per_wan', models.FloatField(verbose_name='万元成本')),
                ('field_management_compliance', models.IntegerField(verbose_name='现场管理符合数')),
            ],
            options={
                'verbose_name': '内控指标汇总',
                'verbose_name_plural': '内控指标汇总',
                'permissions': (('view_internal_control_indicators', '查看内控指标汇总'), ('manage_internal_control_indicators', '管理内控指标汇总')),
            },
        ),
        migrations.CreateModel(
            name='MonthlyFormula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_item', models.CharField(max_length=100, verbose_name='指标')),
                ('formula', models.CharField(max_length=100, verbose_name='公式')),
            ],
            options={
                'verbose_name': '月度绩效考核公式表',
                'verbose_name_plural': '月度绩效考核公式表',
                'permissions': (('manage_formula', '管理报表公式'),),
            },
        ),
        migrations.CreateModel(
            name='MonthlyPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年份')),
                ('month', models.IntegerField(verbose_name='月份')),
                ('delivery_rate', models.FloatField(verbose_name='交付率')),
                ('well_done_rate', models.FloatField(verbose_name='成品率')),
                ('medical_expenses', models.FloatField(verbose_name='医药费')),
                ('overall_cost', models.FloatField(verbose_name='内控综合成本')),
                ('field_management', models.FloatField(verbose_name='现场管理')),
            ],
            options={
                'verbose_name': '月度绩效考核结果',
                'verbose_name_plural': '月度绩效考核结果',
                'permissions': (('view_monthly_performance', '查看月度绩效考核结果'),),
            },
        ),
        migrations.CreateModel(
            name='MonthlySalesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年份')),
                ('month', models.IntegerField(verbose_name='月份')),
                ('turnover', models.FloatField(verbose_name='营业额')),
                ('operating_expenses', models.FloatField(verbose_name='营业费用')),
                ('amount_repaid', models.FloatField(verbose_name='回款额')),
                ('inventory', models.FloatField(verbose_name='库存量')),
                ('profit', models.FloatField(verbose_name='利润额')),
            ],
            options={
                'verbose_name': '月度营业数据',
                'verbose_name_plural': '月度营业数据',
                'permissions': (('view_monthly_sales_data', '查看月度营业数据'), ('manage_monthly_sales_data', '管理月度营业数据')),
            },
        ),
        migrations.CreateModel(
            name='QuarterlyFormula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_item', models.CharField(max_length=100, verbose_name='指标')),
                ('formula', models.CharField(max_length=100, verbose_name='公式')),
            ],
            options={
                'verbose_name': '季度绩效考核公式表',
                'verbose_name_plural': '季度绩效考核公式表',
            },
        ),
        migrations.CreateModel(
            name='QuarterlyPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年份')),
                ('quarter', models.IntegerField(verbose_name='季度')),
                ('turnover', models.FloatField(verbose_name='营业额')),
                ('operating_rate', models.FloatField(null=True, verbose_name='营业费率')),
                ('repaid_rate', models.FloatField(verbose_name='回款率')),
                ('inventory_rate', models.FloatField(null=True, verbose_name='库存率')),
                ('profit_rate', models.FloatField(null=True, verbose_name='利润率')),
            ],
            options={
                'verbose_name': '季度绩效考核结果',
                'verbose_name_plural': '季度绩效考核结果',
                'permissions': (('view_quarterly_performance', '查看季度绩效考核结果'),),
            },
        ),
        migrations.CreateModel(
            name='QuarterlySalesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年份')),
                ('quarter', models.IntegerField(verbose_name='季度')),
                ('turnover', models.FloatField(verbose_name='营业额')),
                ('operating_expenses', models.FloatField(verbose_name='营业费用')),
                ('amount_repaid', models.FloatField(verbose_name='回款额')),
                ('inventory', models.FloatField(verbose_name='库存量')),
                ('profit', models.FloatField(verbose_name='利润额')),
            ],
            options={
                'verbose_name': '季度营业数据',
                'verbose_name_plural': '季度营业数据',
                'permissions': (('view_quarterly_sales_data', '查看季度营业数据'), ('manage_quarterly_sales_data', '管理季度营业数据')),
            },
        ),
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.CharField(max_length=100, verbose_name='工号')),
                ('telephone', models.CharField(max_length=100, verbose_name='电话号码')),
                ('department', models.CharField(max_length=100, verbose_name='部门')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extension', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
