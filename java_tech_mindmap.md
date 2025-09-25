# Java技术栈八股文思维导图

## 1. JUC (Java并发编程)

### 1.1 线程基础
- **线程生命周期**
  - NEW (新建)
  - RUNNABLE (可运行)
  - BLOCKED (阻塞)
  - WAITING (等待)
  - TIMED_WAITING (超时等待)
  - TERMINATED (终止)

- **线程创建方式**
  - 继承Thread类
  - 实现Runnable接口
  - 实现Callable接口
  - 使用线程池

- **线程同步**
  - synchronized关键字
  - volatile关键字
  - wait()/notify()/notifyAll()
  - join()方法
  - yield()方法

### 1.2 线程池
- **核心参数**
  - corePoolSize (核心线程数)
  - maximumPoolSize (最大线程数)
  - keepAliveTime (空闲线程存活时间)
  - workQueue (工作队列)
  - threadFactory (线程工厂)
  - rejectedExecutionHandler (拒绝策略)

- **常见线程池类型**
  - FixedThreadPool (固定大小线程池)
  - CachedThreadPool (缓存线程池)
  - SingleThreadExecutor (单线程执行器)
  - ScheduledThreadPool (定时任务线程池)

- **拒绝策略**
  - AbortPolicy (抛出异常)
  - CallerRunsPolicy (调用者运行)
  - DiscardPolicy (直接丢弃)
  - DiscardOldestPolicy (丢弃最老任务)

### 1.3 锁机制
- **synchronized**
  - 对象锁
  - 类锁
  - 锁升级过程 (偏向锁 → 轻量级锁 → 重量级锁)

- **ReentrantLock**
  - 可重入性
  - 公平锁与非公平锁
  - tryLock()方法
  - lockInterruptibly()方法

- **ReadWriteLock**
  - 读写分离
  - 读锁共享
  - 写锁独占

- **其他锁**
  - StampedLock (乐观读锁)
  - CountDownLatch (倒计时门闩)
  - CyclicBarrier (循环屏障)
  - Semaphore (信号量)

### 1.4 并发集合
- **ConcurrentHashMap**
  - 分段锁机制 (JDK 1.7)
  - CAS + synchronized (JDK 1.8+)
  - 扩容机制

- **CopyOnWriteArrayList**
  - 写时复制
  - 适用场景

- **BlockingQueue**
  - ArrayBlockingQueue (数组阻塞队列)
  - LinkedBlockingQueue (链表阻塞队列)
  - PriorityBlockingQueue (优先级阻塞队列)
  - DelayQueue (延时队列)

### 1.5 原子类
- **基本类型原子类**
  - AtomicInteger
  - AtomicLong
  - AtomicBoolean

- **数组类型原子类**
  - AtomicIntegerArray
  - AtomicLongArray
  - AtomicReferenceArray

- **引用类型原子类**
  - AtomicReference
  - AtomicStampedReference
  - AtomicMarkableReference

- **字段更新器原子类**
  - AtomicIntegerFieldUpdater
  - AtomicLongFieldUpdater
  - AtomicReferenceFieldUpdater

## 2. JVM (Java虚拟机)

### 2.1 内存模型
- **程序计数器 (PC Register)**
  - 当前线程执行字节码行号指示器
  - 线程私有
  - 唯一不会OutOfMemoryError的区域

- **虚拟机栈 (JVM Stack)**
  - 线程私有
  - 存储局部变量表、操作数栈、动态链接、方法出口
  - StackOverflowError和OutOfMemoryError

- **本地方法栈 (Native Method Stack)**
  - 为Native方法服务
  - HotSpot虚拟机中与虚拟机栈合二为一

- **堆 (Heap)**
  - 所有线程共享
  - 存放对象实例
  - 分为新生代和老年代
  - 新生代: Eden + Survivor0 + Survivor1

- **方法区 (Method Area)**
  - 存储类信息、常量、静态变量、即时编译器编译后的代码
  - JDK 8之前为永久代，JDK 8之后为元空间(Metaspace)

- **直接内存 (Direct Memory)**
  - 不属于JVM运行时数据区
  - NIO中使用的堆外内存

### 2.2 垃圾回收
- **判断对象是否存活**
  - 引用计数法 (存在循环引用问题)
  - 可达性分析算法 (GC Roots)

- **GC Roots对象**
  - 虚拟机栈中引用的对象
  - 方法区中静态属性引用的对象
  - 方法区中常量引用的对象
  - 本地方法栈中引用的对象

- **垃圾收集算法**
  - 标记-清除算法 (Mark-Sweep)
  - 复制算法 (Copying)
  - 标记-整理算法 (Mark-Compact)
  - 分代收集算法

- **垃圾收集器**
  - Serial收集器 (单线程)
  - ParNew收集器 (多线程版Serial)
  - Parallel Scavenge收集器 (吞吐量优先)
  - Serial Old收集器
  - Parallel Old收集器
  - CMS收集器 (并发标记清除)
  - G1收集器 (低延迟)
  - ZGC收集器 (超低延迟)

### 2.3 类加载
- **类加载过程**
  - 加载 (Loading)
  - 验证 (Verification)
  - 准备 (Preparation)
  - 解析 (Resolution)
  - 初始化 (Initialization)

- **类加载器**
  - 启动类加载器 (Bootstrap ClassLoader)
  - 扩展类加载器 (Extension ClassLoader)
  - 应用程序类加载器 (Application ClassLoader)
  - 自定义类加载器

- **双亲委派模型**
  - 工作流程
  - 破坏双亲委派模型的场景
  - 优点和缺点

### 2.4 性能调优
- **JVM参数**
  - 堆内存设置 (-Xms, -Xmx)
  - 新生代设置 (-Xmn, -XX:NewRatio)
  - 垃圾收集器选择
  - GC日志配置

- **性能监控工具**
  - jps (Java进程状态)
  - jstat (JVM统计监测)
  - jmap (内存映像)
  - jstack (Java堆栈跟踪)
  - jhsdb (Java堆快速数据库)

- **常见调优策略**
  - 内存溢出问题排查
  - CPU使用率过高排查
  - GC频繁问题优化
  - 内存泄漏检测

## 3. Redis

### 3.1 数据结构
- **String (字符串)**
  - 底层实现: SDS (Simple Dynamic String)
  - 应用场景: 缓存、计数器、分布式锁

- **Hash (哈希)**
  - 底层实现: ziplist + hashtable
  - 应用场景: 对象存储、购物车

- **List (列表)**
  - 底层实现: quicklist (ziplist + linkedlist)
  - 应用场景: 消息队列、最新消息

- **Set (集合)**
  - 底层实现: intset + hashtable
  - 应用场景: 标签、好友关系

- **Zset (有序集合)**
  - 底层实现: ziplist + skiplist + hashtable
  - 应用场景: 排行榜、延时队列

- **高级数据类型**
  - Bitmap (位图)
  - HyperLogLog (基数统计)
  - Geospatial (地理位置)
  - Stream (流)

### 3.2 持久化
- **RDB (Redis Database)**
  - 全量快照
  - save和bgsave命令
  - 优缺点分析

- **AOF (Append Only File)**
  - 增量日志
  - 三种同步策略: always, everysec, no
  - AOF重写机制

- **混合持久化**
  - RDB + AOF
  - Redis 4.0新特性

### 3.3 集群
- **主从复制**
  - 复制流程
  - 全量复制和增量复制
  - 主从切换

- **Sentinel (哨兵)**
  - 监控、通知、故障转移
  - 选举机制
  - 脑裂问题

- **Cluster (集群)**
  - 分片机制
  - 槽位分配
  - 集群扩容和缩容
  - 故障检测和转移

### 3.4 缓存策略
- **缓存更新策略**
  - Cache Aside Pattern
  - Read Through
  - Write Through
  - Write Behind

- **缓存问题**
  - 缓存穿透 (布隆过滤器、空值缓存)
  - 缓存击穿 (热点数据过期)
  - 缓存雪崩 (大量key同时过期)

- **一致性保证**
  - 最终一致性
  - 强一致性
  - 延时双删

### 3.5 分布式锁
- **实现方式**
  - SETNX + EXPIRE
  - SET EX PX NX
  - Lua脚本
  - Redisson框架

- **锁的特性**
  - 互斥性
  - 安全性
  - 死锁检测
  - 容错性

## 4. RocketMQ

### 4.1 消息模型
- **角色组成**
  - Producer (生产者)
  - Consumer (消费者)
  - NameServer (路由注册中心)
  - Broker (消息代理)

- **消息类型**
  - 普通消息
  - 顺序消息
  - 事务消息
  - 延时消息
  - 批量消息

- **Topic和Queue**
  - Topic (主题)
  - MessageQueue (消息队列)
  - 负载均衡策略

### 4.2 集群部署
- **NameServer集群**
  - 无状态设计
  - 路由信息管理
  - 服务发现

- **Broker集群**
  - Master-Slave模式
  - 同步复制和异步复制
  - 刷盘策略

- **部署架构**
  - 单Master模式
  - 多Master模式
  - 多Master多Slave模式

### 4.3 事务消息
- **实现原理**
  - Half消息
  - 事务状态回查
  - 最终一致性

- **使用场景**
  - 分布式事务
  - 数据最终一致性
  - 业务解耦

### 4.4 顺序消息
- **全局顺序**
  - 单个Topic只有一个MessageQueue
  - 性能限制

- **局部顺序**
  - 按业务key分区
  - MessageQueueSelector
  - 顺序消费

### 4.5 高可用机制
- **消息重试**
  - 生产者重试
  - 消费者重试
  - 死信队列

- **消息幂等**
  - 业务幂等
  - 去重机制

- **流量控制**
  - 生产者流控
  - 消费者流控
  - Broker流控

## 5. MySQL

### 5.1 索引
- **索引类型**
  - B+Tree索引 (InnoDB默认)
  - Hash索引 (Memory引擎)
  - 全文索引 (FULLTEXT)
  - 空间索引 (SPATIAL)

- **索引分类**
  - 主键索引 (聚簇索引)
  - 唯一索引
  - 普通索引
  - 复合索引
  - 覆盖索引

- **索引优化**
  - 最左前缀原则
  - 索引下推
  - 索引合并
  - 索引选择性

### 5.2 事务
- **ACID特性**
  - Atomicity (原子性)
  - Consistency (一致性)
  - Isolation (隔离性)
  - Durability (持久性)

- **隔离级别**
  - READ UNCOMMITTED (读未提交)
  - READ COMMITTED (读已提交)
  - REPEATABLE READ (可重复读)
  - SERIALIZABLE (串行化)

- **并发问题**
  - 脏读 (Dirty Read)
  - 不可重复读 (Non-Repeatable Read)
  - 幻读 (Phantom Read)

### 5.3 锁机制
- **锁粒度**
  - 表级锁
  - 行级锁
  - 页级锁

- **锁类型**
  - 共享锁 (S锁)
  - 排他锁 (X锁)
  - 意向锁 (IS锁、IX锁)

- **InnoDB锁**
  - Record Lock (记录锁)
  - Gap Lock (间隙锁)
  - Next-Key Lock (临键锁)

- **死锁**
  - 死锁检测
  - 死锁处理
  - 死锁预防

### 5.4 性能优化
- **查询优化**
  - EXPLAIN执行计划
  - 索引优化
  - SQL重写
  - 分页优化

- **配置优化**
  - 缓冲池配置
  - 连接数配置
  - 日志配置
  - 存储引擎选择

- **架构优化**
  - 分库分表
  - 读写分离
  - 缓存策略
  - 连接池

### 5.5 主从复制
- **复制原理**
  - binlog (二进制日志)
  - relay log (中继日志)
  - 异步复制、半同步复制

- **复制格式**
  - Statement格式
  - Row格式
  - Mixed格式

- **复制延迟**
  - 产生原因
  - 监控方法
  - 优化策略

### 5.6 分库分表
- **垂直拆分**
  - 垂直分库
  - 垂直分表

- **水平拆分**
  - 水平分库
  - 水平分表

- **分片策略**
  - 范围分片
  - 哈希分片
  - 目录分片

- **跨库查询**
  - 分布式事务
  - 数据聚合
  - 分页查询

---

## 常见面试问题汇总

### JUC相关
1. synchronized和ReentrantLock的区别？
2. ThreadLocal的实现原理和内存泄漏问题？
3. ConcurrentHashMap的实现原理？
4. 线程池的核心参数和工作流程？
5. AQS的实现原理？

### JVM相关
1. JVM内存结构和各区域的作用？
2. 垃圾回收算法和收集器的特点？
3. 类加载机制和双亲委派模型？
4. 如何排查内存溢出问题？
5. JVM调优的常用参数？

### Redis相关
1. Redis的数据结构和底层实现？
2. Redis持久化机制RDB和AOF的区别？
3. Redis集群的实现方式？
4. 如何解决缓存穿透、击穿、雪崩问题？
5. Redis分布式锁的实现？

### RocketMQ相关
1. RocketMQ的架构组成和工作流程？
2. 如何保证消息的可靠性传输？
3. 顺序消息和事务消息的实现原理？
4. 如何处理消息重复消费问题？
5. RocketMQ和Kafka的区别？

### MySQL相关
1. InnoDB和MyISAM存储引擎的区别？
2. B+Tree索引的优势和实现原理？
3. MySQL事务的ACID特性如何实现？
4. 如何优化慢查询？
5. 主从复制的原理和延迟问题？

---

*本思维导图涵盖了Java后端开发中最重要的技术栈知识点，适合面试准备和日常技术学习使用。建议结合实际项目经验进行深入理解和实践。*