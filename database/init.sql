-- 创建测试数据（可选）
INSERT INTO api_teacher (name, office_location)
VALUES (
    '张老师',
    ST_GeomFromText('POINT(116.397526 39.908692)', 4326)
);

INSERT INTO api_student (name, student_id, status)
VALUES 
    ('张三', '20230001', 'active'),
    ('李四', '20230002', 'graduated');
