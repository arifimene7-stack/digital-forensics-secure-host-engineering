# Network-Process Correlation

## Objective
Correlate network connections with the processes responsible for them.

## Evidence Sources

The following evidence was collected:

- `ss -tunap`
- `ss -lntup`
- `lsof -i -n -P`

## Observed Services

Examples of observed network activity include:

| Process | PID | Activity |
|---|---:|---|
| systemd-resolved | 470 | Local DNS |
| avahi-daemon | 1446 | mDNS |
| chronyd | 1581 | Time synchronization |
| NetworkManager | 1589 | DHCP |
| cupsd | 1693 | Local printing service |
| dnsmasq | 2045 | libvirt networking |
| Firefox | 5068 | HTTPS connections |
| QEMU | 42094 | VM-related network activity |

## QEMU Network Activity

QEMU PID 42094 had:

- localhost SPICE listener on `127.0.0.1:5900`
- an outbound connection attempt to `198.51.100.20:7680`
- several HTTPS connections to remote IP addresses
- connections in states including `ESTAB`, `SYN-SENT` and `CLOSE-WAIT`

The QEMU command line also showed user-mode networking configured for the virtual machine.

## Interpretation

The presence of a remote IP address does not by itself indicate malicious activity.

The observed QEMU connections must be interpreted together with the process command line and virtualization configuration.

Because the Windows guest was using QEMU user-mode networking, host-side QEMU network activity cannot be automatically attributed to a specific application inside the Windows guest.

Guest-side telemetry would be required for that level of attribution.

## Other Network Activity

Firefox generated multiple HTTPS connections, which is consistent with normal browser activity.

Local services such as DNS, CUPS, Avahi and libvirt networking were also observed.

## Assessment

No clearly malicious network activity was identified from the collected host-side evidence.

The QEMU network activity should be treated as virtualization-related activity unless additional evidence establishes otherwise.

## Limitations

The analysis is based on a point-in-time host snapshot.

Remote IP addresses were not independently attributed to organizations or domains during this investigation.

The evidence does not provide complete visibility into network activity occurring inside the Windows guest.
