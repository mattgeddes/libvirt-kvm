#!/usr/bin/env python

class FilterModule( object ):
    def filters( self ):
        return {
                'ipmac': self.ipmac
        }

    def ipmac( self, ipaddr, hvid ):
        """
        This filter takes an IP address and a hypervisor ID and generates a 
        valid MAC address that contains both the IP address (bottom 4 bytes)
        and the hypervisor ID embedded.
        """
        local_bit = 2 # locally-administered MAC address bit
        octets = ipaddr.split( "." )
        ipmac = "%02x:%02x:%02x:%02x:%02x:%02x" % (
                int( local_bit ),
                int( hvid ),
                int( octets[0] ),
                int( octets[1] ),
                int( octets[2] ),
                int( octets[3] )
                )

        return ipmac

