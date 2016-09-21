<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output
	encoding="UTF-8"	
	indent="yes"/>
    
    <xsl:strip-space elements="*"/>
    
    <xsl:template match="/">
        <!-- authors: Sina Bock and Philip Duerholt -->
        <!-- date: Independence Day 2016 -->
        <!-- version: end of hello world -->
        
        <toc>
            <xsl:apply-templates/>
        </toc>
    </xsl:template>
    
    <xsl:template match="li">
        <topic>
            <xsl:apply-templates/>
        </topic>
    </xsl:template>
    
    <xsl:template match="a">
        <xsl:attribute name="href">https://wiki.de.dariah.eu<xsl:value-of select="@href"/>
        </xsl:attribute>
        <xsl:attribute name="label"><xsl:value-of select="translate(normalize-space(text()), '&#xA;', '')"/>
        </xsl:attribute>
    </xsl:template>
    
<!--    href="<xsl:value-of select="//div[@type = 'essay']/head[1]"/>"
    -->
<!--    
    <xsl:template match="li">
        <xsl:for-each select="a">
            <topic>
                <xsl:attribute name="href">https://wiki.de.dariah.eu<xsl:value-of select="@href"/>
                </xsl:attribute>
                <xsl:apply-templates/>
            </topic>
        </xsl:for-each>    
    </xsl:template>
    -->
    
<!--    <xsl:template match="li">
        <topic>
            <xsl:attribute name="href">https://wiki.de.dariah.eu<xsl:value-of select="@href"/>
            </xsl:attribute>
        </topic>
    </xsl:template>-->
<!--    
    <xsl:template match="li/a">
        <topic>
            <xsl:attribute name="href">https://wiki.de.dariah.eu<xsl:value-of select="@href"/>
            </xsl:attribute>
        </topic>
    </xsl:template>-->
    
<!--    <xsl:template match="li">
        <topic>
            <xsl:apply-templates/>
        </topic>
    </xsl:template>-->
    
</xsl:stylesheet>