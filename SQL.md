## 1. Get all statuses, not repeating, alphabetically ordered
```sql
SELECT DISTINCT status
FROM task_manager_task
ORDER BY status ASC;
```

## 2. Get the count of all tasks in each project, order by tasks count descending
```sql
SELECT p.name AS project_name, COUNT(t.id) AS task_count
FROM task_manager_project p
LEFT JOIN task_manager_task t ON p.id = t.project_id
GROUP BY p.id, p.name
ORDER BY task_count DESC;
```

## 3. Get the count of all tasks in each project, order by task_manager_project names
```sql
SELECT p.name AS project_name, COUNT(t.id) AS task_count
FROM task_manager_project p
LEFT JOIN task_manager_task t ON p.id = t.project_id
GROUP BY p.id, p.name
ORDER BY p.name ASC;
```

## 4. Get the task_manager_task for all task_manager_project having the name beginning with "N" letter
```sql
SELECT t.*
FROM task_manager_task t
JOIN task_manager_project p ON t.project_id = p.id
WHERE p.name LIKE 'N%';
```

## 5. Get the list of all task_manager_project containing the 'a' letter in the middle of the name, and show the tasks count near each project.
```sql
SELECT p.name AS project_name, COUNT(t.id) AS task_count
FROM task_manager_project p
LEFT JOIN task_manager_task t ON p.id = t.project_id
WHERE p.name ~ '^.{1,}a.{1,}$'
GROUP BY p.id, p.name;
```

## 6. Get the list of tasks with duplicate names. Order alphabetically
```sql
SELECT name
FROM task_manager_task
GROUP BY name
HAVING COUNT(*) > 1
ORDER BY name ASC;
```

## 7. Get the list of tasks having several exact matches of both name and status, from the project 'Delivery’. Order by matches count
```sql
SELECT t.name, t.status, COUNT(*) AS match_count
FROM task_manager_task t
JOIN task_manager_project p ON t.project_id = p.id
WHERE p.name = 'Delivery'
GROUP BY t.name, t.status
HAVING COUNT(*) > 1
ORDER BY match_count DESC;
```

## 8. Get the list of project names having more than 10 tasks in status 'completed'. Order by project_id
```sql
SELECT p.name
FROM task_manager_project p
JOIN task_manager_task t ON p.id = t.project_id
WHERE t.status = 'completed'
GROUP BY p.id, p.name
HAVING COUNT(t.id) > 10
ORDER BY p.id ASC;
```