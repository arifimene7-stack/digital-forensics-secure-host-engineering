# Process Investigation Report

## 1. Which process did you choose?
The chosen process is: **xdg-document-portal**
- **PID:** 3341
- **User:** imene

## 2. Who is the Parent Process?
The parent process is Process ID **1** (which is `systemd`). You can verify this by running `ps -fp 3341` and looking at the PPID column.

## 3. What is PID?
PID stands for "Process ID". It is a unique number given to every running process in the system. In our case, the PID is **3341**.

## 4. What is PPID?
PPID stands for "Parent Process ID". It is the ID number of the process that started the current process.

## 5. What are its child processes?
Since it is a daemon process for file management, it may not have direct child processes. You can check by running:
`pstree -p 3341`

## 6. What files are open?
These are the open File Descriptors for this process. You can see them by running:
`ls -l /proc/3341/fd`
You will usually see `socket`, `pipe`, and `anon_inode` files. This means it is waiting for requests from other applications.

## 7. Does it have a Network connection/socket?
**No, it does not have external network connections.**
If you search the output of `sudo ss -tunap`, you will not find the number 3341 or the name `xdg-document-po` in the connection list. It only uses local connections (Unix Sockets) to talk to other parts of the system.

## 8. Why is it considered normal?
It is normal because `xdg-document-portal` is a system service in Linux desktop environments (like GNOME). Its job is to allow applications (like browsers or text editors) to open and save files safely, without giving them full permissions to the file system. Having no network connections is very normal because its function is purely local.

## 9. What evidence supports this conclusion?
- The process name itself, `xdg-document-portal`, indicates its function (document management).
- The owner user is `imene` (not root), which means it runs in the user session.
- "لم يظهر له اتصال شبكي خارجي في لقطة الأدلة التي تم جمعها"
