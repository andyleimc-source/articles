---
type: mixed
density: per-section
style: notion
image_count: 12
---

# 配图大纲 — AI 时代的软件工程原则

## Illustration 00 (Cover)
**Position**: 文章顶部封面
**Purpose**: 代表"AI × 工程原则"整体主题，11条原则围绕中心
**Visual Content**: 中央"11 Principles"框架，周围排列11个编号图标
**Filename**: 00-framework-cover.png

## Illustration 01
**Position**: 原则1「分步拆解」之后
**Purpose**: 可视化"规划→配置→执行"三阶段流程
**Visual Content**: 三步骤水平流程图，Strategy→Config→Execute
**Filename**: 01-flowchart-decomposition.png

## Illustration 02
**Position**: 原则2「硬约束前置过滤」之后
**Purpose**: 对比"AI处理所有情况" vs "代码先过滤，AI只处理可行选项"
**Visual Content**: 左右对比，左边乱糟糟（全量输入AI），右边整洁（代码过滤后AI）
**Filename**: 02-comparison-hard-constraint.png

## Illustration 03
**Position**: 原则3「步间校验」之后
**Purpose**: 可视化数据在步骤间流动，校验作为"过滤网"
**Visual Content**: 线性流程，每个步骤之间有一个校验门
**Filename**: 03-flowchart-validation.png

## Illustration 04
**Position**: 原则4「隔离性」之后
**Purpose**: 展示多个任务并行，单个失败不影响其他
**Visual Content**: 多个并行通道，一个通道标红失败，其他保持绿色
**Filename**: 04-framework-isolation.png

## Illustration 05
**Position**: 原则5「降级优先」之后
**Purpose**: 可视化"局部错误被吸收，系统继续运行"
**Visual Content**: 系统接受错误输入，降级处理后输出可用结果
**Filename**: 05-infographic-degradation.png

## Illustration 06
**Position**: 原则6「幂等性」之后
**Purpose**: 展示"无论执行1次还是N次，结果相同"
**Visual Content**: 同一操作执行3次，结果始终一致
**Filename**: 06-infographic-idempotency.png

## Illustration 07
**Position**: 原则7「断点续跑」之后
**Purpose**: 可视化checkpoint机制，中断后从断点恢复
**Visual Content**: 时间轴，中途有断点标记，恢复后从断点继续而非从头
**Filename**: 07-timeline-checkpoint.png

## Illustration 08
**Position**: 原则8「干跑」之后
**Purpose**: 对比"真实执行有副作用" vs "Dry Run安全无副作用"
**Visual Content**: 左右对比，左边执行有真实数据产生，右边Dry Run输出计划不产生数据
**Filename**: 08-comparison-dry-run.png

## Illustration 09
**Position**: 原则9「可观测性」之后
**Purpose**: 展示可观测性仪表盘，显示耗时、token、成功率
**Visual Content**: 简洁仪表盘风格，显示各步骤指标
**Filename**: 09-infographic-observability.png

## Illustration 10
**Position**: 原则10「限流与并发控制」之后
**Purpose**: 展示信号量控制并发，避免冲垮外部API
**Visual Content**: 多个请求通过"控制阀"流向API，控制流速
**Filename**: 10-framework-rate-limit.png

## Illustration 11
**Position**: 原则11「回滚」之后
**Purpose**: 展示两种策略选择：保留已成功 vs 全部回滚
**Visual Content**: 分叉路口，两条路分别标注两种策略
**Filename**: 11-comparison-rollback.png
